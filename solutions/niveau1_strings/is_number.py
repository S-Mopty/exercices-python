"""Solution — is_number (niveau 1)."""


def is_number(text: str) -> bool:
    if len(text) == 0:
        return False
    start = 0
    if text[0] == '-':
        start = 1
    if start == len(text):          # le texte était juste "-"
        return False
    for i in range(start, len(text)):
        if not ('0' <= text[i] <= '9'):
            return False            # un seul intrus suffit
    return True
