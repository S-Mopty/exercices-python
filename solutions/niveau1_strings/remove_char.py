"""Solution — remove_char (niveau 1)."""


def remove_char(text: str, c: str) -> str:
    result = ""
    for ch in text:
        if ch != c:             # on ne recopie que ce qu'on garde
            result = result + ch
    return result
