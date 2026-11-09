"""Solution — count_digit (niveau 3)."""


def count_digit(n: int, d: int) -> int:
    if n < 10:                              # un seul chiffre
        if n == d:
            return 1
        return 0
    last = 0
    if n % 10 == d:
        last = 1
    return last + count_digit(n // 10, d)   # dernier chiffre + le reste
