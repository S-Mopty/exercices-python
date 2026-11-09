"""Solution — crack_caesar (niveau 6)."""


def decode(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            c = chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            c = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        result = result + c
    return result


def score(text: str) -> int:
    count = 0
    for c in text:
        if 'A' <= c <= 'Z':
            c = chr(ord(c) - ord('A') + ord('a'))
        if c in "etaoin":
            count = count + 1
    return count


def crack_caesar(cipher: str) -> int:
    best_shift = 0
    best_score = score(cipher)          # décalage 0
    for s in range(1, 26):
        current = score(decode(cipher, s))
        if current > best_score:        # > strict : en cas d'égalité on garde le plus petit
            best_score = current
            best_shift = s
    return best_shift
