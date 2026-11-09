"""Solution — alternate_case (niveau 2)."""


def alternate_case(text: str) -> str:
    result = ""
    letter_index = 0                 # n'avance QUE sur les lettres
    for c in text:
        is_upper = 'A' <= c <= 'Z'
        is_lower = 'a' <= c <= 'z'
        if is_upper or is_lower:
            if letter_index % 2 == 0:            # rang pair -> majuscule
                if is_lower:
                    c = chr(ord(c) - ord('a') + ord('A'))
            else:                                # rang impair -> minuscule
                if is_upper:
                    c = chr(ord(c) - ord('A') + ord('a'))
            letter_index = letter_index + 1
        result = result + c
    return result
