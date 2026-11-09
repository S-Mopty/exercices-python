"""Solution — binary_words (niveau 4)."""


def _gen(prefix: str, remaining: int) -> int:
    """Affiche tous les mots qui commencent par prefix et auxquels il manque
    `remaining` caractères. Renvoie combien il y en a."""
    if remaining == 0:
        print(prefix)
        return 1
    with_0 = _gen(prefix + "0", remaining - 1)   # d'abord toute la branche 0
    with_1 = _gen(prefix + "1", remaining - 1)   # puis toute la branche 1
    return with_0 + with_1


def binary_words(n: int) -> int:
    if n < 0:
        raise ValueError("Invalid length")
    return _gen("", n)
