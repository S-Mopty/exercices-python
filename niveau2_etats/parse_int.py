"""
parse_int — Niveau 2 ★★★

Écris `parse_int(text)` qui convertit `text` en entier, SANS utiliser
int(). Le texte peut commencer par un '-'.
Si le texte n'est pas un entier valide (vide, "-" seul, caractère qui n'est
pas un chiffre, '-' ailleurs qu'au début, '+'...) : lever ValueError.

Exemples
    parse_int("1234")  ->  1234
    parse_int("-56")   ->  -56
    parse_int("007")   ->  7
    parse_int("12a")   ->  ValueError
    parse_int("")      ->  ValueError

Contraintes
    - boucle obligatoire
    - int() interdit (c'est tout l'exercice)

Indice
    La valeur d'un chiffre c, c'est ord(c) - ord('0').
    Lis de gauche à droite en gardant le résultat partiel :
        "123" :  0  ->  0*10 + 1 = 1  ->  1*10 + 2 = 12  ->  12*10 + 3 = 123
    Le signe se gère à part (une variable `negative`), à la toute fin.
    Tu peux t'inspirer de ton is_number du niveau 1 pour la validation.

Vérifier : python3 check.py parse_int
"""


def parse_int(text: str) -> int:
    pass


if __name__ == "__main__":
    print(parse_int("-56") + 1)
