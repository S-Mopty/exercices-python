"""
from_base — Niveau 3 ★★★

L'inverse du to_base du TP : écris `from_base(digits, base)` qui convertit
la chaîne `digits`, écrite en base `base` (2 <= base <= 16), en entier.
Les chiffres au-delà de 9 sont les majuscules 'A' à 'F'.

Lever ValueError si `digits` est vide, ou contient un caractère qui n'est
pas un chiffre valide DANS CETTE BASE (ex : '2' en base 2, 'G', ou 'f'
minuscule).

Exemples
    from_base("1010", 2)   ->  10
    from_base("FF", 16)    ->  255
    from_base("777", 8)    ->  511
    from_base("0", 5)      ->  0
    from_base("102", 2)    ->  ValueError
    from_base("", 10)      ->  ValueError

Contraintes
    - récursive, aucune boucle
    - int() interdit (int("FF", 16) ferait tout le travail...)

Indice
    Lis "1011" de gauche à droite :
        valeur("1011") = valeur("101") * 2 + 1
    Sans slicing, « le préfixe de longueur i » se représente par un
    indice : helper _value(digits, i, base) = valeur des i premiers
    caractères. Cas de base : i == 0 -> 0.
    Écris aussi un helper _digit_value(c) qui renvoie 0..15 (ou -1 si
    ce n'est pas un chiffre hexadécimal majuscule).

Vérifier : python3 check.py from_base
"""


def from_base(digits: str, base: int) -> int:
    pass


if __name__ == "__main__":
    print(from_base("FF", 16))
