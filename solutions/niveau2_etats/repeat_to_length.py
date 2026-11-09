"""Solution — repeat_to_length (niveau 2)."""


def repeat_to_length(pattern: str, n: int) -> str:
    if len(pattern) == 0 or n < 0:
        raise ValueError("Invalid argument")
    result = ""
    for i in range(n):
        result = result + pattern[i % len(pattern)]   # l'indice « boucle »
    return result
