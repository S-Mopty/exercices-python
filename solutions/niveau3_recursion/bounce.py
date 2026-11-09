"""Solution — bounce (niveau 3)."""


def bounce(n: int) -> int:
    if n <= 0:
        return 0
    print(n)                    # à l'aller  : n, n-1, ..., 1
    lines = bounce(n - 1)       # le sous-problème affiche ses lignes et les compte
    print(n)                    # au retour  : 1, 2, ..., n
    return lines + 2            # ses lignes + mes 2 lignes
