"""Solution — digit_shift / digit_unshift (niveau 2)."""


def shift_letter(c: str, d: int) -> str:
    """Décale la lettre c de d positions (d peut être négatif)."""
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + d) % 26 + ord('a'))
    if 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + d) % 26 + ord('A'))
    return c


def is_letter(c: str) -> bool:
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'


def apply_key(text: str, key: str, direction: int) -> str:
    """direction = 1 pour chiffrer, -1 pour déchiffrer."""
    if len(key) == 0:
        raise ValueError("Empty key")
    result = ""
    k = 0                                   # index dans la clé
    for c in text:
        if is_letter(c):
            d = ord(key[k % len(key)]) - ord('0')
            result = result + shift_letter(c, direction * d)
            k = k + 1                       # la clé n'avance que sur les lettres
        else:
            result = result + c
    return result


def digit_shift(text: str, key: str) -> str:
    return apply_key(text, key, 1)


def digit_unshift(text: str, key: str) -> str:
    return apply_key(text, key, -1)
