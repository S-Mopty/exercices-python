"""Solution — compress (niveau 2)."""


def compress(text: str) -> str:
    if len(text) == 0:
        return ""
    result = ""
    current = text[0]          # caractère du bloc en cours
    count = 0                  # longueur du bloc en cours
    for c in text:
        if c == current:
            count = count + 1
        else:                  # le bloc précédent est terminé : on l'écrit
            result = result + current + str(count)
            current = c
            count = 1
    # le dernier bloc n'a jamais été « fermé » par un changement
    return result + current + str(count)
