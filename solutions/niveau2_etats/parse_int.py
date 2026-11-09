"""Solution — parse_int (niveau 2)."""


def parse_int(text: str) -> int:
    if len(text) == 0:
        raise ValueError("Invalid number")
    negative = False
    start = 0
    if text[0] == '-':
        negative = True
        start = 1
    if start == len(text):                       # juste "-"
        raise ValueError("Invalid number")
    result = 0
    for i in range(start, len(text)):
        c = text[i]
        if not ('0' <= c <= '9'):
            raise ValueError("Invalid number")
        result = result * 10 + (ord(c) - ord('0'))   # schéma de Horner
    if negative:
        result = -result
    return result
