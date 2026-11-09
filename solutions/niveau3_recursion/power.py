"""Solution — power (niveau 3)."""


def power(x: int, n: int) -> int:
    if n < 0:
        raise ValueError("Negative exponent")
    if n == 0:                       # cas de base : x^0 = 1
        return 1
    return x * power(x, n - 1)       # x^n = x * x^(n-1)


def fast_power(x: int, n: int) -> int:
    """Bonus : environ log2(n) appels au lieu de n."""
    if n == 0:
        return 1
    half = fast_power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x
