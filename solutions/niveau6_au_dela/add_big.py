"""Solution — add_big (niveau 6)."""


def _check(s: str) -> None:
    if len(s) == 0:
        raise ValueError("Empty number")
    for c in s:
        if not ('0' <= c <= '9'):
            raise ValueError("Invalid digit")


def add_big(a: str, b: str) -> str:
    _check(a)
    _check(b)
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""
    while i >= 0 or j >= 0 or carry > 0:
        total = carry
        if i >= 0:
            total = total + ord(a[i]) - ord('0')
        if j >= 0:
            total = total + ord(b[j]) - ord('0')
        result = chr(total % 10 + ord('0')) + result   # on écrit DEVANT
        carry = total // 10
        i = i - 1
        j = j - 1
    return result
