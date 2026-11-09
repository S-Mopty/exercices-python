"""
remove_char — Niveau 1 ★

Écris `remove_char(text, c)` qui renvoie une copie de `text` dans laquelle
toutes les occurrences du caractère `c` ont été supprimées.

Exemples
    remove_char("b-a-n-a-n-a", "-")  ->  "banana"
    remove_char("hello", "l")        ->  "heo"
    remove_char("abc", "z")          ->  "abc"
    remove_char("", "a")             ->  ""

Contraintes
    - boucle obligatoire, résultat construit par concaténation
    - pas de .replace()

Vérifier : python3 check.py remove_char
"""


def remove_char(text: str, c: str) -> str:
    pass


if __name__ == "__main__":
    print(remove_char("b-a-n-a-n-a", "-"))
