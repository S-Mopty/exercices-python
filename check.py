#!/usr/bin/env python3
"""
check.py — correcteur automatique, façon moulinette.

Utilisation (depuis le dossier du dépôt) :

    python3 check.py                     # tous les exercices
    python3 check.py 3                   # tout le niveau 3
    python3 check.py compress            # un seul exercice
    python3 check.py compress ruler      # plusieurs exercices
    python3 check.py --express           # seulement le parcours express

Sous Windows, remplace `python3` par `python` (ou `py`).

Pour chaque exercice, le correcteur :
  1. vérifie les règles (pas de méthodes, pas de slicing, pas de listes,
     récursion obligatoire si demandée, etc.) ;
  2. lance une série de tests (valeurs de retour, affichages, exceptions,
     entrées clavier simulées) ;
  3. te dit précisément ce qui ne va pas.

Un exercice dont la fonction contient encore seulement `pass` est marqué
« À FAIRE » : ce n'est pas une erreur.
"""

import ast
import builtins
import contextlib
import importlib.util
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from tests.framework import NO_CHECK, Custom  # noqa: E402
from tests import (  # noqa: E402
    niveau1, niveau2, niveau3, niveau4, niveau5, niveau6,
)

LEVELS = [niveau1.LEVEL, niveau2.LEVEL, niveau3.LEVEL,
          niveau4.LEVEL, niveau5.LEVEL, niveau6.LEVEL]

ALLOWED_BUILTINS = {"print", "len", "int", "str", "input", "ord", "chr",
                    "range", "ValueError"}
BUILTIN_NAMES = set(dir(builtins))
TIMEOUT_S = 10
MAX_FAILS_SHOWN = 3
RESULT_MARK = "@@CHECK_RESULT@@"


# --------------------------------------------------------------------------
# Analyse statique (les règles « moulinette »)
# --------------------------------------------------------------------------

def _is_main_guard(stmt):
    return (isinstance(stmt, ast.If)
            and isinstance(stmt.test, ast.Compare)
            and isinstance(stmt.test.left, ast.Name)
            and stmt.test.left.id == "__name__")


class _StripAnnotations(ast.NodeTransformer):
    """Les annotations (`text: str`, `-> bool`) ne comptent pas comme du code."""

    def visit_FunctionDef(self, node):
        node.returns = None
        a = node.args
        for arg in a.posonlyargs + a.args + a.kwonlyargs:
            arg.annotation = None
        if a.vararg:
            a.vararg.annotation = None
        if a.kwarg:
            a.kwarg.annotation = None
        self.generic_visit(node)
        return node

    def visit_AnnAssign(self, node):
        node.annotation = ast.Constant(value=None)
        self.generic_visit(node)
        return node


def _defined_names(tree):
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            names.add(node.id)
        elif isinstance(node, ast.FunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.arg):
            names.add(node.arg)
    return names


GENERIC_BANS = [
    ((ast.Import, ast.ImportFrom), "import interdit"),
    ((ast.Slice,), "slicing `s[a:b]` interdit"),
    ((ast.List, ast.ListComp), "listes interdites"),
    ((ast.Dict, ast.DictComp), "dictionnaires interdits"),
    ((ast.Set, ast.SetComp), "sets interdits"),
    ((ast.Tuple,), "tuples interdits (ex : `a, b = b, a` -> passe par une "
                   "variable temporaire ; `return a, b` -> impossible ici)"),
    ((ast.GeneratorExp,), "expressions génératrices interdites"),
    ((ast.Lambda,), "lambda interdit"),
    ((ast.Global, ast.Nonlocal), "`global` / `nonlocal` interdits : fais "
                                 "remonter l'information avec `return`"),
]


def generic_violations(tree):
    """Règles valables pour tous les exercices."""
    found = {}
    defined = _defined_names(tree)
    body = [s for s in tree.body if not _is_main_guard(s)]
    for stmt in body:
        for node in ast.walk(stmt):
            line = getattr(node, "lineno", 0)
            for types, msg in GENERIC_BANS:
                if isinstance(node, types):
                    found.setdefault((line, msg), None)
            if isinstance(node, ast.Attribute):
                found.setdefault(
                    (line, "`.%s` interdit : pas de méthodes ni d'attributs "
                           "(pas de .lower(), .split(), .count()...)" % node.attr),
                    None)
            if (isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load)
                    and node.id in BUILTIN_NAMES
                    and node.id not in ALLOWED_BUILTINS
                    and node.id not in defined
                    and node.id not in ("True", "False", "None")):
                found.setdefault(
                    (line, "`%s` non autorisé (builtins autorisés : print, len, "
                           "int, str, input, ord, chr, range, ValueError)" % node.id),
                    None)
    return sorted(found)


def _all_functions(tree):
    funcs = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcs.setdefault(node.name, node)
    return funcs


def _call_graph(funcs):
    graph = {}
    for name, fdef in funcs.items():
        called = set()
        for node in ast.walk(fdef):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in funcs:
                    called.add(node.func.id)
        graph[name] = called
    return graph


def _reachable(start, graph, strict=False):
    seen = set()
    todo = list(graph.get(start, ())) if strict else [start]
    while todo:
        cur = todo.pop()
        if cur in seen:
            continue
        seen.add(cur)
        todo.extend(graph.get(cur, ()))
    return seen


def rule_violations(tree, fname, rules):
    """Règles propres à l'exercice, appliquées à la fonction et à ses helpers."""
    funcs = _all_functions(tree)
    if fname not in funcs:
        return []
    graph = _call_graph(funcs)
    reach = _reachable(fname, graph)
    nodes = []
    for f in reach:
        nodes.extend(ast.walk(funcs[f]))
    msgs = []

    loops = [n for n in nodes if isinstance(n, (ast.For, ast.While))]
    if rules.get("must_loop") and not loops:
        msgs.append("`%s` doit utiliser une boucle (for ou while)" % fname)
    if rules.get("no_loop") and loops:
        msgs.append("ligne %d : boucle interdite dans `%s` (et ses helpers) — "
                    "exercice de récursion" % (loops[0].lineno, fname))
    if rules.get("must_recurse"):
        if not any(g in _reachable(g, graph, strict=True) for g in reach):
            msgs.append("`%s` doit être récursive : elle (ou un de ses "
                        "helpers) doit s'appeler elle-même" % fname)
    if rules.get("no_index"):
        subs = [n for n in nodes if isinstance(n, ast.Subscript)]
        if subs:
            msgs.append("ligne %d : indexation `s[i]` interdite dans cet "
                        "exercice" % subs[0].lineno)
    if rules.get("no_pow"):
        pows = [n for n in nodes
                if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow)]
        if pows:
            msgs.append("ligne %d : `**` interdit dans cet exercice"
                        % pows[0].lineno)
    if rules.get("no_in"):
        ins = [n for n in nodes if isinstance(n, ast.Compare)
               and any(isinstance(op, (ast.In, ast.NotIn)) for op in n.ops)]
        if ins:
            msgs.append("ligne %d : `in` / `not in` interdit dans une "
                        "condition ici" % ins[0].lineno)
    if rules.get("no_str_mult"):
        for n in nodes:
            if (isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult)
                    and any(isinstance(side, ast.Constant)
                            and isinstance(side.value, str)
                            for side in (n.left, n.right))):
                msgs.append("ligne %d : répétition `\"x\" * n` interdite : "
                            "construis la chaîne morceau par morceau" % n.lineno)
                break
    for banned in rules.get("ban_names", ()):
        uses = [n for n in nodes if isinstance(n, ast.Name)
                and n.id == banned and isinstance(n.ctx, ast.Load)]
        if uses:
            msgs.append("ligne %d : `%s` interdit dans cet exercice"
                        % (uses[0].lineno, banned))
    return msgs


def is_stub(fdef):
    """Vrai si le corps de la fonction n'est que docstring / pass / ... ."""
    real = [s for s in fdef.body
            if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant))]
    return all(isinstance(s, ast.Pass) for s in real)


# --------------------------------------------------------------------------
# Exécution des tests (processus enfant)
# --------------------------------------------------------------------------

class OutOfInput(BaseException):
    """Le programme a demandé une entrée de trop."""


class InputFeeder:
    """Remplace input() : affiche le prompt, « tape » la ligne et la ré-affiche
    comme dans un vrai terminal."""

    def __init__(self, lines):
        self.lines = list(lines)
        self.pos = 0

    def __call__(self, prompt=""):
        sys.stdout.write(str(prompt))
        if self.pos >= len(self.lines):
            raise OutOfInput()
        line = self.lines[self.pos]
        self.pos += 1
        sys.stdout.write(line + "\n")
        return line


def _same(got, expected):
    return type(got) is type(expected) and got == expected


def _short(value, limit=300):
    text = repr(value)
    return text if len(text) <= limit else text[:limit] + "..."


def _block(text, limit=25):
    if text == "":
        return ["      (rien)"]
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    shown = lines[:limit]
    out = ["      | " + line for line in shown]
    if len(lines) > limit:
        out.append("      | ... (%d lignes de plus)" % (len(lines) - limit))
    return out


def _diff_out(expected, got):
    msg = ["sortie attendue :"] + _block(expected)
    msg += ["    sortie obtenue :"] + _block(got)
    exp_lines = expected.split("\n")
    got_lines = got.split("\n")
    for i in range(max(len(exp_lines), len(got_lines))):
        e = exp_lines[i] if i < len(exp_lines) else None
        g = got_lines[i] if i < len(got_lines) else None
        if e != g:
            if e is None:
                detail = "ligne en trop : %r" % g
            elif g is None:
                detail = "ligne manquante : %r" % e
            else:
                detail = "attendu %r, obtenu %r" % (e, g)
            msg.append("    -> première différence ligne %d : %s" % (i + 1, detail))
            break
    return "\n".join(msg)


def run_case(module, case):
    """Renvoie None si le cas passe, sinon un message d'erreur."""
    fn = getattr(module, case.func)
    call = "%s(%s)" % (case.func, ", ".join(_short(a, 80) for a in case.args))
    if case.inputs is not None:
        call += "   [entrées tapées : %s]" % ", ".join(repr(x) for x in case.inputs)
    buf = io.StringIO()
    old_input = builtins.input
    builtins.input = InputFeeder(case.inputs or [])
    ret, exc = None, None
    try:
        with contextlib.redirect_stdout(buf):
            ret = fn(*case.args)
    except BaseException as e:  # noqa: BLE001 — on veut tout attraper
        exc = e
    finally:
        builtins.input = old_input
    out = buf.getvalue()

    if case.raises is not None:
        name = case.raises.__name__
        if isinstance(exc, case.raises):
            return None
        if exc is None:
            return "%s\n    devait lever %s, mais a renvoyé %s" % (call, name, _short(ret))
        return "%s\n    devait lever %s, mais a levé %s: %s" % (
            call, name, type(exc).__name__, exc)

    if exc is not None:
        if isinstance(exc, RecursionError):
            why = ("RecursionError : récursion infinie ? (cas de base manquant, "
                   "ou jamais atteint)")
        elif isinstance(exc, OutOfInput):
            why = ("le programme a demandé plus d'entrées que prévu (il ne "
                   "s'arrête pas quand il devrait ?)")
        else:
            why = "a planté : %s: %s" % (type(exc).__name__, exc)
        msg = "%s\n    %s" % (call, why)
        if out:
            msg += "\n    affichage avant le plantage :\n" + "\n".join(_block(out))
        return msg

    problems = []
    if case.out is not None and out != case.out:
        problems.append(_diff_out(case.out, out))
    if case.ret is not NO_CHECK and not _same(ret, case.ret):
        line = "renvoie %s au lieu de %s" % (_short(ret), _short(case.ret))
        if ret is None and case.out is None and str(case.ret) in out:
            line += "  (tu as fait print() au lieu de return ?)"
        elif ret is not None and case.ret is not None and ret == case.ret:
            line += "  (bon contenu, mauvais type : %s au lieu de %s)" % (
                type(ret).__name__, type(case.ret).__name__)
        problems.append(line)
    if problems:
        return call + "\n    " + "\n    ".join(problems)
    return None


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    buf = io.StringIO()
    old_input = builtins.input
    builtins.input = InputFeeder([])
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(module)
    finally:
        builtins.input = old_input
    return module, buf.getvalue()


def evaluate(level, ex, base_dir):
    res = {"status": "ok", "messages": [], "notes": []}
    path = os.path.join(base_dir, level.folder, ex.file)
    if not os.path.exists(path):
        res["status"] = "error"
        res["messages"].append("fichier introuvable : %s" % os.path.relpath(path, ROOT))
        return res
    with open(path, encoding="utf-8") as f:
        source = f.read()
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        res["status"] = "error"
        res["messages"].append("erreur de syntaxe ligne %s : %s" % (e.lineno, e.msg))
        return res
    tree = _StripAnnotations().visit(tree)

    top_funcs = {s.name: s for s in tree.body if isinstance(s, ast.FunctionDef)}
    missing = [f for f in ex.funcs if f not in top_funcs]
    if missing:
        res["status"] = "error"
        res["messages"].append("fonction(s) introuvable(s) : %s (ne change pas les "
                               "noms ni les prototypes)" % ", ".join(missing))
        return res

    try:
        module, import_out = load_module(path, "student_" + ex.name)
    except BaseException as e:  # noqa: BLE001
        res["status"] = "error"
        res["messages"].append("le fichier plante dès l'import : %s: %s"
                               % (type(e).__name__, e))
        return res

    if ex.todo_check is not None:
        todo, total = ex.todo_check(module)
    else:
        todo = [f for f in ex.funcs if is_stub(top_funcs[f])]
        total = len(ex.funcs)
    if len(todo) == total:
        res["status"] = "todo"
        return res
    done = [f for f in ex.funcs if f not in todo]

    if import_out:
        res["notes"].append("ton fichier affiche du texte dès l'import : mets tes "
                            "tests perso sous `if __name__ == \"__main__\":`")

    violations = ["ligne %d : %s" % (line, msg) for line, msg in generic_violations(tree)]
    for f in done:
        violations += rule_violations(tree, f, ex.rules)
    res["messages"] += ["règle non respectée — " + v for v in violations]

    fails = []
    for case in ex.cases:
        if isinstance(case, Custom):
            err = case.fn(module)
            if err:
                fails.append("%s\n    %s" % (case.label, err))
            continue
        if case.func not in done:
            continue
        err = run_case(module, case)
        if err:
            fails.append(err)
    if fails:
        # Le premier échec en détail : on corrige une chose à la fois.
        res["messages"].append(fails[0])
        others = [f.split("\n")[0] for f in fails[1:]]
        if others:
            shown = others[:MAX_FAILS_SHOWN]
            line = "aussi en échec : " + " ; ".join(shown)
            if len(others) > MAX_FAILS_SHOWN:
                line += " ; ... (+%d)" % (len(others) - MAX_FAILS_SHOWN)
            res["messages"].append(line)
    if violations or fails:
        res["status"] = "fail"
    elif todo:
        res["status"] = "partial"
        res["notes"].append("encore à faire : %s" % ", ".join(todo))
    return res


def child_main(level_no, ex_name, base_dir):
    level = [lv for lv in LEVELS if lv.number == level_no][0]
    ex = [e for e in level.exercises if e.name == ex_name][0]
    try:
        res = evaluate(level, ex, base_dir)
    except BaseException as e:  # noqa: BLE001
        res = {"status": "error", "messages": ["erreur interne du correcteur : %r" % e],
               "notes": []}
    sys.__stdout__.write("\n" + RESULT_MARK + json.dumps(res) + "\n")
    sys.__stdout__.flush()


# --------------------------------------------------------------------------
# Affichage (processus parent)
# --------------------------------------------------------------------------

def _setup_terminal():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    use_color = sys.stdout.isatty() and not os.environ.get("NO_COLOR")
    if use_color and os.name == "nt":
        os.system("")  # active les couleurs ANSI dans le terminal Windows
    return use_color


COLORS = {"ok": "32", "fail": "31", "error": "31", "todo": "33",
          "partial": "36", "title": "1", "dim": "2"}
LABELS = {"ok": "OK", "fail": "ÉCHEC", "error": "ERREUR", "todo": "À FAIRE",
          "partial": "PARTIEL"}


def run_in_child(level, ex, base_dir):
    cmd = [sys.executable, os.path.abspath(__file__), "--child",
           str(level.number), ex.name, base_dir]
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    try:
        proc = subprocess.run(cmd, capture_output=True, timeout=TIMEOUT_S, env=env,
                              cwd=ROOT)
    except subprocess.TimeoutExpired:
        return {"status": "fail", "notes": [],
                "messages": ["TIMEOUT (> %d s) : boucle infinie ? (une variable "
                             "qui n'avance pas dans un while, par exemple)" % TIMEOUT_S]}
    stdout = proc.stdout.decode("utf-8", errors="replace")
    for line in reversed(stdout.splitlines()):
        if line.startswith(RESULT_MARK):
            return json.loads(line[len(RESULT_MARK):])
    err = proc.stderr.decode("utf-8", errors="replace").strip().splitlines()
    return {"status": "error", "notes": [],
            "messages": ["le correcteur n'a pas pu tester ce fichier : %s"
                         % (err[-1] if err else "raison inconnue")]}


def select(args):
    express = "--express" in args
    names = [a for a in args if not a.startswith("--")]
    all_ex = [(lv, ex) for lv in LEVELS for ex in lv.exercises]
    if not names:
        chosen = all_ex
    else:
        chosen = []
        for name in names:
            stem = name[:-3] if name.endswith(".py") else name
            stem = os.path.basename(stem)
            if stem.isdigit():
                hits = [(lv, ex) for lv, ex in all_ex if lv.number == int(stem)]
            else:
                hits = [(lv, ex) for lv, ex in all_ex
                        if ex.name == stem or ex.file[:-3] == stem
                        or stem in ex.funcs]
            if not hits:
                print("Exercice ou niveau inconnu : %r" % name)
                print("Exercices disponibles : "
                      + ", ".join(ex.name for _, ex in all_ex))
                sys.exit(2)
            chosen += [h for h in hits if h not in chosen]
    if express:
        chosen = [(lv, ex) for lv, ex in chosen if ex.express]
    return chosen


def parent_main(args):
    color = _setup_terminal()

    def paint(text, kind):
        return "\033[%sm%s\033[0m" % (COLORS[kind], text) if color else text

    base_dir = ROOT
    if "--solutions" in args:
        base_dir = os.path.join(ROOT, "solutions")
    for arg in args:
        if arg.startswith("--dir="):
            base_dir = os.path.abspath(arg[len("--dir="):])
    chosen = select(args)
    counts = {"ok": 0, "fail": 0, "error": 0, "todo": 0, "partial": 0}
    next_up = None
    current_level = None
    for level, ex in chosen:
        if level is not current_level:
            current_level = level
            print()
            print(paint("Niveau %d — %s" % (level.number, level.title), "title"))
        res = run_in_child(level, ex, base_dir)
        status = res["status"]
        counts[status] += 1
        if status != "ok" and next_up is None:
            next_up = ex.name
        stars = "★" * ex.stars
        express = " (express)" if ex.express else ""
        print("  %s %-22s %s%s" % (paint("%-8s" % LABELS[status], status),
                                   ex.name, stars, paint(express, "dim")))
        for msg in res["messages"]:
            lines = msg.split("\n")
            print("           x " + lines[0])
            for extra in lines[1:]:
                print("           " + extra)
        for note in res["notes"]:
            print(paint("           note : " + note, "dim"))
    total = len(chosen)
    print()
    print(paint("Bilan : %d/%d réussis · %d en échec · %d à faire"
                % (counts["ok"], total, counts["fail"] + counts["error"],
                   counts["todo"] + counts["partial"]), "title"))
    if next_up and total > 1:
        print("Prochain exercice conseillé : %s   ->  python3 check.py %s"
              % (next_up, next_up))
    elif total and counts["ok"] == total:
        print("Tout est vert. Bien joué.")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--child":
        child_main(int(sys.argv[2]), sys.argv[3], sys.argv[4])
    else:
        parent_main(sys.argv[1:])
