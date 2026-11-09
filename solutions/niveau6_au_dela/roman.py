"""Solution — to_roman / from_roman (niveau 6)."""


def _repeat(symbol: str, k: int) -> str:
    result = ""
    for _ in range(k):
        result = result + symbol
    return result


def _digit(d: int, one: str, five: str, ten: str) -> str:
    """Écrit le chiffre décimal d (0..9) avec les symboles du rang voulu."""
    if d == 9:
        return one + ten
    if d >= 5:
        return five + _repeat(one, d - 5)
    if d == 4:
        return one + five
    return _repeat(one, d)


def to_roman(n: int) -> str:
    if n < 1 or n > 3999:
        raise ValueError("Out of range")
    return (_repeat("M", n // 1000)
            + _digit(n // 100 % 10, "C", "D", "M")
            + _digit(n // 10 % 10, "X", "L", "C")
            + _digit(n % 10, "I", "V", "X"))


def _value(c: str) -> int:
    if c == 'I':
        return 1
    if c == 'V':
        return 5
    if c == 'X':
        return 10
    if c == 'L':
        return 50
    if c == 'C':
        return 100
    if c == 'D':
        return 500
    if c == 'M':
        return 1000
    raise ValueError("Invalid roman digit")


def from_roman(s: str) -> int:
    if len(s) == 0:
        raise ValueError("Empty")
    total = 0
    for i in range(len(s)):
        v = _value(s[i])
        if i + 1 < len(s) and v < _value(s[i + 1]):
            total = total - v           # IV : le I se soustrait
        else:
            total = total + v
    return total
