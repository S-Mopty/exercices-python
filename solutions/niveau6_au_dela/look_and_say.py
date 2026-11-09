"""Solution — look_and_say (niveau 6)."""


def describe(term: str) -> str:
    """Le terme suivant : compress, avec le compte AVANT le chiffre."""
    result = ""
    current = term[0]
    count = 0
    for c in term:
        if c == current:
            count = count + 1
        else:
            result = result + str(count) + current
            current = c
            count = 1
    return result + str(count) + current


def look_and_say(n: int) -> str:
    if n < 1:
        raise ValueError("Invalid index")
    term = "1"
    for _ in range(n - 1):
        term = describe(term)
    return term
