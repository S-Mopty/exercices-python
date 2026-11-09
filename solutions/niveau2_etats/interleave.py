"""Solution — interleave (niveau 2)."""


def interleave(a: str, b: str) -> str:
    longest = len(a)
    if len(b) > longest:
        longest = len(b)
    result = ""
    for i in range(longest):
        if i < len(a):
            result = result + a[i]
        if i < len(b):
            result = result + b[i]
    return result
