"""Solution — reverse_rec (niveau 3)."""


def _reverse_from(text: str, i: int) -> str:
    """Inverse de la partie de text qui commence à l'indice i."""
    if i == len(text):
        return ""
    return _reverse_from(text, i + 1) + text[i]


def reverse_rec(text: str) -> str:
    return _reverse_from(text, 0)
