"""Solution — first_index / last_index (niveau 1)."""


def first_index(text: str, c: str) -> int:
    for i in range(len(text)):
        if text[i] == c:
            return i            # trouvé : on s'arrête tout de suite
    return -1                   # on n'arrive ici que si on n'a rien trouvé


def last_index(text: str, c: str) -> int:
    # Version 1 : on parcourt à l'envers, et le premier trouvé est le dernier.
    for i in range(len(text) - 1, -1, -1):
        if text[i] == c:
            return i
    return -1


def last_index_v2(text: str, c: str) -> int:
    # Version 2 : on parcourt tout, en mémorisant le dernier indice vu.
    last = -1
    for i in range(len(text)):
        if text[i] == c:
            last = i
    return last
