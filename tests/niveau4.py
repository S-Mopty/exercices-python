import contextlib
import io

from tests.framework import Case as C, Custom, Exercise, Level

REC = {"must_recurse": True, "no_loop": True}


# ---- predict : les fonctions mystère de référence (copie non modifiable) ----

def _a(n):
    if n == 0:
        return
    _a(n - 1)
    print(n)
    _a(n - 1)


def _b(n):
    if n >= 10:
        _b(n // 10)
    print(n % 10)


def _c(n):
    if n <= 1:
        return 1
    return _c(n - 1) + _c(n - 2)


def _c_calls(n):
    if n <= 1:
        return 1
    return 1 + _c_calls(n - 1) + _c_calls(n - 2)


def _d(n, x, y):
    if n > 0:
        _d(n - 1, y, x)
        print(x + y)
        _d(n - 1, y, x)


def _e(n):
    if n == 0:
        return 0
    print(n)
    r = _e(n - 1)
    print(r)
    return r + n


def _shown(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*args)
    return " ".join(buf.getvalue().split())


def _quiet(fn, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*args)


QUESTIONS = [
    # (numéro, type, valeur attendue, indice en cas d'erreur)
    (1, "out", _shown(_a, 3),
     "mystery_a(1) affiche « 1 ». Écris ce qu'affiche mystery_a(2), puis "
     "sers-t'en pour mystery_a(3)."),
    (2, "out", _shown(_b, 907),
     "le print est APRÈS l'appel récursif : qui affiche en premier ?"),
    (3, "ret", _quiet(_c, 5),
     "calcule mystery_c(0), (1), (2)... dans l'ordre, du bas vers le haut."),
    (4, "ret", _c_calls(5),
     "dessine l'arbre des appels de mystery_c(5) et compte TOUS les nœuds."),
    (5, "out", _shown(_d, 2, "A", "B"),
     "regarde bien : l'appel récursif reçoit (y, x), pas (x, y)."),
    (6, "out", _shown(_d, 3, "A", "B"),
     "commence par écrire ce qu'affiche mystery_d(2, \"B\", \"A\")."),
    (7, "out", _shown(_e, 3),
     "à l'aller on affiche n ; au retour on affiche ce que l'appel du "
     "dessous a RENVOYÉ."),
    (8, "ret", _quiet(_e, 3),
     "e(0) renvoie 0. Que renvoie e(1) ? e(2) ?"),
]


def _make_check(num, kind, expected, hint):
    def check(module):
        got = getattr(module, "PREDICTION_%d" % num, None)
        if got is None:
            return None
        if kind == "ret":
            if type(got) is not int:
                return "attendu : un int (ex : 8), pas %r" % (got,)
            if got != expected:
                return "faux. Indice : " + hint
            return None
        if type(got) is not str:
            return "attendu : une chaîne, ex : \"1 2 3\""
        if " ".join(got.split()) != expected:
            return "faux. Indice : " + hint
        return None
    return check


def _predict_todo(module):
    todo = [q[0] for q in QUESTIONS
            if getattr(module, "PREDICTION_%d" % q[0], None) is None]
    return ["Q%d" % n for n in todo], len(QUESTIONS)


PREDICT_CASES = [Custom(_make_check(*q), "Q%d" % q[0]) for q in QUESTIONS]


HANOI_3 = ("disk 1: L -> R\ndisk 2: L -> M\ndisk 1: R -> M\ndisk 3: L -> R\n"
           "disk 1: M -> L\ndisk 2: M -> R\ndisk 1: L -> R\n")


def _hanoi_ref(n, src, aux, dst, lines):
    if n == 0:
        return
    _hanoi_ref(n - 1, src, dst, aux, lines)
    lines.append("disk %d: %s -> %s" % (n, src, dst))
    _hanoi_ref(n - 1, aux, src, dst, lines)


def _hanoi_out(n, src, aux, dst):
    lines = []
    _hanoi_ref(n, src, aux, dst, lines)
    return "".join(line + "\n" for line in lines)


def _ruler_out(n):
    if n == 0:
        return ""
    return _ruler_out(n - 1) + "-" * n + "\n" + _ruler_out(n - 1)


def _binary_out(n):
    return "".join(format(i, "0%db" % n) + "\n" for i in range(2 ** n)) if n else "\n"


EXERCISES = [
    Exercise("predict", "predict.py", [], stars=2, express=True,
             todo_check=_predict_todo, cases=PREDICT_CASES),
    Exercise("ruler", "ruler.py", ["ruler"], stars=2, express=True,
             rules={"must_recurse": True, "no_pow": True, "no_str_mult": True},
             cases=[
        C("ruler", (1,), 1, out="-\n"),
        C("ruler", (2,), 3, out="-\n--\n-\n"),
        C("ruler", (3,), 7, out=_ruler_out(3)),
        C("ruler", (0,), 0, out=""),
        C("ruler", (5,), 31, out=_ruler_out(5)),
        C("ruler", (-1,), raises=ValueError),
    ]),
    Exercise("binary_words", "binary_words.py", ["binary_words"], stars=3,
             express=True, rules=dict(REC, no_pow=True), cases=[
        C("binary_words", (2,), 4, out="00\n01\n10\n11\n"),
        C("binary_words", (1,), 2, out="0\n1\n"),
        C("binary_words", (3,), 8, out=_binary_out(3)),
        C("binary_words", (0,), 1, out="\n"),
        C("binary_words", (4,), 16, out=_binary_out(4)),
        C("binary_words", (-1,), raises=ValueError),
    ]),
    Exercise("grid_paths", "grid_paths.py", ["grid_paths"], stars=3,
             rules=REC, cases=[
        C("grid_paths", (2, 2), 6),
        C("grid_paths", (1, 3), 4),
        C("grid_paths", (0, 5), 1),
        C("grid_paths", (5, 0), 1),
        C("grid_paths", (3, 3), 20),
        C("grid_paths", (0, 0), 1),
        C("grid_paths", (4, 6), 210),
        C("grid_paths", (-1, 2), raises=ValueError),
        C("grid_paths", (2, -1), raises=ValueError),
    ]),
    Exercise("fibo", "fibo.py", ["fibo", "fibo_calls"], stars=3, rules=REC,
             cases=[
        C("fibo", (0,), 0),
        C("fibo", (1,), 1),
        C("fibo", (2,), 1),
        C("fibo", (10,), 55),
        C("fibo", (15,), 610),
        C("fibo", (-1,), raises=ValueError),
        C("fibo_calls", (0,), 1),
        C("fibo_calls", (1,), 1),
        C("fibo_calls", (2,), 3),
        C("fibo_calls", (5,), 15),
        C("fibo_calls", (10,), 177),
        C("fibo_calls", (-1,), raises=ValueError),
    ]),
    Exercise("hanoi", "hanoi.py", ["hanoi"], stars=4, express=True,
             rules=dict(REC, no_pow=True), cases=[
        C("hanoi", (1, "A", "B", "C"), 1, out="disk 1: A -> C\n"),
        C("hanoi", (2, "A", "B", "C"), 3,
          out="disk 1: A -> B\ndisk 2: A -> C\ndisk 1: B -> C\n"),
        C("hanoi", (3, "L", "M", "R"), 7, out=HANOI_3),
        C("hanoi", (0, "A", "B", "C"), 0, out=""),
        C("hanoi", (4, "X", "Y", "Z"), 15, out=_hanoi_out(4, "X", "Y", "Z")),
        C("hanoi", (3, "C", "A", "B"), 7, out=_hanoi_out(3, "C", "A", "B")),
        C("hanoi", (-1, "A", "B", "C"), raises=ValueError),
    ]),
    Exercise("permutations", "permutations.py", ["permutations"], stars=4,
             rules={"must_recurse": True}, cases=[
        C("permutations", ("abc",), 6, out="abc\nacb\nbac\nbca\ncab\ncba\n"),
        C("permutations", ("ab",), 2, out="ab\nba\n"),
        C("permutations", ("x",), 1, out="x\n"),
        C("permutations", ("",), 1, out="\n"),
        C("permutations", ("1234",), 24, out=(
            "1234\n1243\n1324\n1342\n1423\n1432\n2134\n2143\n2314\n2341\n"
            "2413\n2431\n3124\n3142\n3214\n3241\n3412\n3421\n4123\n4132\n"
            "4213\n4231\n4312\n4321\n")),
    ]),
]

LEVEL = Level(4, "niveau4_recursion_multiple",
              "Récursion à plusieurs appels : la route vers Hanoï", EXERCISES)
