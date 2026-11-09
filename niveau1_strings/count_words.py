"""
count_words — Niveau 1 ★★   (pont vers le niveau 2)

Écris `count_words(text)` qui renvoie le nombre de mots de `text`.
Les mots sont séparés par UN OU PLUSIEURS espaces, et il peut y avoir des
espaces au début et à la fin.

Exemples
    count_words("hello world")          ->  2
    count_words("  hello   world  ")    ->  2
    count_words("one")                  ->  1
    count_words("     ")                ->  0
    count_words("")                     ->  0

Contraintes
    - boucle obligatoire
    - pas de .split() (évidemment)

Indice
    Compter les espaces ne marche pas (essaie sur "  a  b " pour t'en
    convaincre). Ce qu'il faut compter, ce sont les DÉBUTS de mots : un
    caractère qui n'est pas un espace et qui suit un espace (ou le début).
    Garde en mémoire, d'un tour de boucle à l'autre, une variable
    `in_word` (booléen) qui dit si tu es en train de lire un mot.
    -> Cette idée de « variable qui se souvient du tour précédent », c'est
       tout le sujet du niveau 2.

Vérifier : python3 check.py count_words
"""


def count_words(text: str) -> int:
    pass


if __name__ == "__main__":
    print(count_words("  hello   world  "))
