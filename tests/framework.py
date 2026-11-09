"""Briques de base des tests. Tu n'as pas besoin de lire ce fichier."""

NO_CHECK = object()


class Case:
    """Un appel de fonction à tester.

    func    : nom de la fonction à appeler
    args    : arguments (tuple)
    ret     : valeur de retour attendue (NO_CHECK = on ne vérifie pas)
    out     : sortie standard attendue, au caractère près (None = on ne vérifie pas)
    inputs  : lignes « tapées au clavier » (pour les exercices avec input())
    raises  : exception attendue (ex: ValueError)
    """

    def __init__(self, func, args=(), ret=NO_CHECK, out=None, inputs=None,
                 raises=None):
        self.func = func
        self.args = args
        self.ret = ret
        self.out = out
        self.inputs = inputs
        self.raises = raises


class Custom:
    """Vérification sur mesure : fn(module) renvoie None si OK, sinon un message."""

    def __init__(self, fn, label):
        self.fn = fn
        self.label = label


class Exercise:
    """Un exercice = un fichier + les fonctions attendues + des règles + des cas.

    rules (par fonction attendue, appliquées à elle ET à ses helpers) :
        must_loop     : au moins un for/while
        no_loop       : aucun for/while
        must_recurse  : la fonction (ou un de ses helpers) doit s'appeler elle-même
        no_index      : pas de s[i]
        no_pow        : pas de **
        no_in         : pas de `x in s` / `x not in s` dans une condition
        no_str_mult   : pas de "#" * n
        ban_names     : builtins supplémentaires interdits, ex: ["len"]
    """

    def __init__(self, name, file, funcs, cases, rules=None, stars=1,
                 express=False, todo_check=None):
        self.name = name
        self.file = file
        self.funcs = funcs
        self.cases = cases
        self.rules = rules or {}
        self.stars = stars
        self.express = express
        self.todo_check = todo_check


class Level:
    def __init__(self, number, folder, title, exercises):
        self.number = number
        self.folder = folder
        self.title = title
        self.exercises = exercises
