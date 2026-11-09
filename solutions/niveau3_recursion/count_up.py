"""Solution — count_up (niveau 3)."""


def count_up(n: int) -> None:
    if n <= 0:              # cas de base : rien à afficher
        return
    count_up(n - 1)         # d'abord : 1, 2, ..., n-1
    print(n)                # puis n, « au retour »
