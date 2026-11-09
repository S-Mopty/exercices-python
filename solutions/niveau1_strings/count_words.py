"""Solution — count_words (niveau 1)."""


def count_words(text: str) -> int:
    count = 0
    in_word = False             # état : est-on en train de lire un mot ?
    for c in text:
        if c == ' ':
            in_word = False
        elif not in_word:       # non-espace juste après un espace : début de mot
            count = count + 1
            in_word = True
    return count
