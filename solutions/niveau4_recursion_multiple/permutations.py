"""Solution — permutations (niveau 4)."""


def _without(s: str, i: int) -> str:
    """s privé de son caractère d'indice i."""
    result = ""
    for j in range(len(s)):
        if j != i:
            result = result + s[j]
    return result


def _perm(prefix: str, rest: str) -> int:
    if len(rest) == 0:
        print(prefix)
        return 1
    count = 0
    for i in range(len(rest)):          # une branche par caractère disponible
        count = count + _perm(prefix + rest[i], _without(rest, i))
    return count


def permutations(text: str) -> int:
    return _perm("", text)
