"""
reverse_rec — Niveau 3 ★★

Écris `reverse_rec(text)` qui renvoie `text` à l'envers, de façon
RÉCURSIVE.

Exemples
    reverse_rec("hello")   ->  "olleh"
    reverse_rec("ab cd")   ->  "dc ba"
    reverse_rec("")        ->  ""

Contraintes
    - récursive, aucune boucle
    - pas de slicing (donc pas de text[1:])
    - l'indexation text[i] est autorisée

Indice
    Sans slicing, impossible de « raccourcir » la chaîne à chaque appel.
    La parade, à retenir absolument : un HELPER avec un paramètre en plus.
        def _reverse_from(text, i):
            # renvoie l'inverse de la partie de text qui commence à l'indice i
    Cas de base : i == len(text) (il ne reste rien).
    Cas récursif : l'inverse de « text[i] suivi du reste », c'est
    « l'inverse du reste » suivi de text[i].
    Puis reverse_rec(text) se contente d'appeler _reverse_from(text, 0).
    -> Hanoï utilise le même principe : la fonction demandée appelle un
       helper qui a plus de paramètres (les noms des tours).

Vérifier : python3 check.py reverse_rec
"""


def reverse_rec(text: str) -> str:
    pass


if __name__ == "__main__":
    print(reverse_rec("hello"))
