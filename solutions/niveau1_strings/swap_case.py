"""Solution — swap_case (niveau 1)."""


def swap_case(text: str) -> str:
    result = ""
    for c in text:
        if 'A' <= c <= 'Z':
            result = result + chr(ord(c) - ord('A') + ord('a'))
        elif 'a' <= c <= 'z':
            result = result + chr(ord(c) - ord('a') + ord('A'))
        else:
            result = result + c
    return result
