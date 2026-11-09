"""Solution — from_base (niveau 3)."""


def _digit_value(c: str) -> int:
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    if 'A' <= c <= 'F':
        return ord(c) - ord('A') + 10
    return -1


def _value(digits: str, i: int, base: int) -> int:
    """Valeur des i premiers caractères de digits."""
    if i == 0:
        return 0
    d = _digit_value(digits[i - 1])
    if d < 0 or d >= base:
        raise ValueError("Invalid digit")
    return _value(digits, i - 1, base) * base + d


def from_base(digits: str, base: int) -> int:
    if len(digits) == 0:
        raise ValueError("Empty number")
    return _value(digits, len(digits), base)
