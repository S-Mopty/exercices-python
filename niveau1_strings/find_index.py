"""
find_index — Niveau 1 ★  (deux fonctions dans ce fichier)

1) `first_index(text, c)` renvoie l'indice de la PREMIÈRE occurrence du
   caractère `c` dans `text`, ou -1 s'il n'y est pas.

2) `last_index(text, c)` renvoie l'indice de la DERNIÈRE occurrence, ou -1.

Exemples
    first_index("banana", "n")  ->  2
    first_index("banana", "z")  ->  -1
    last_index("banana", "a")   ->  5
    last_index("banana", "b")   ->  0
    last_index("", "a")         ->  -1

Contraintes
    - boucle obligatoire dans chaque fonction
    - pas de .find() / .index() / .rfind()

Indice
    first_index : parcours les indices avec range(len(text)) et fais
    `return i` dès que tu trouves — inutile d'aller plus loin.
    last_index : deux options. Soit tu parcours à l'envers
    (range(len(text) - 1, -1, -1)), soit tu parcours tout et tu
    mémorises le dernier indice vu. Essaie les deux.

Vérifier : python3 check.py find_index
"""


def first_index(text: str, c: str) -> int:
    pass


def last_index(text: str, c: str) -> int:
    pass


if __name__ == "__main__":
    print(first_index("banana", "n"))
    print(last_index("banana", "a"))
