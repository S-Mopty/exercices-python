"""Solution — find_sub (niveau 2)."""


def find_sub(text: str, pattern: str) -> int:
    for i in range(len(text) - len(pattern) + 1):   # positions de départ possibles
        match = True
        j = 0
        while j < len(pattern) and match:
            if text[i + j] != pattern[j]:
                match = False
            j = j + 1
        if match:
            return i
    return -1
