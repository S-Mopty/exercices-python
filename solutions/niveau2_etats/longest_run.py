"""Solution — longest_run (niveau 2)."""


def longest_run(text: str) -> int:
    best = 0          # meilleure suite vue jusqu'ici
    current = 0       # suite en cours
    previous = ""     # caractère du tour précédent ("" = aucun)
    for c in text:
        if c == previous:
            current = current + 1
        else:
            current = 1
        if current > best:
            best = current
        previous = c
    return best
