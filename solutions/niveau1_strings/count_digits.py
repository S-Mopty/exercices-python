"""Solution — count_digits (niveau 1)."""


def count_digits(text: str) -> int:
    count = 0                                   # accumulateur
    for c in text:
        if ord('0') <= ord(c) <= ord('9'):      # comparaison chaînée
            count = count + 1
    return count
