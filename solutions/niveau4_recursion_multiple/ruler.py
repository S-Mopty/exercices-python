"""Solution — ruler (niveau 4)."""


def _dashes(n: int) -> str:
    line = ""
    for _ in range(n):
        line = line + "-"
    return line


def ruler(n: int) -> int:
    if n < 0:
        raise ValueError("Invalid size")
    if n == 0:
        return 0
    left = ruler(n - 1)          # la moitié gauche se débrouille seule...
    print(_dashes(n))            # ... ma graduation, au milieu...
    right = ruler(n - 1)         # ... et la moitié droite pareil.
    return left + 1 + right
