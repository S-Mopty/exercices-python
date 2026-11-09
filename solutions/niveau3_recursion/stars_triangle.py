"""Solution — stars_triangle (niveau 3)."""


def _stars(k: int) -> str:
    """Renvoie une chaîne de k étoiles (sans rien afficher)."""
    if k <= 0:
        return ""
    return "*" + _stars(k - 1)


def stars_triangle(n: int) -> int:
    if n <= 0:
        return 0
    total = stars_triangle(n - 1)   # d'abord les lignes 1..n-1
    print(_stars(n))                # puis ma ligne
    return total + n
