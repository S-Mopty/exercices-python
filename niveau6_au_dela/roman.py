"""
roman — Niveau 6 ★★★  (deux fonctions dans ce fichier)

Chiffres romains : I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
Un symbole placé AVANT un symbole plus grand se soustrait :
IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900.

1) `to_roman(n)` : entier -> chiffres romains, pour 1 <= n <= 3999.
   Sinon : lever ValueError.
2) `from_roman(s)` : chiffres romains -> entier. Lever ValueError si `s`
   est vide ou contient un caractère qui n'est pas un symbole romain.
   (On ne vérifie pas que l'écriture est « canonique » : "IIII" -> 4 accepté.)

Exemples
    to_roman(1994)          ->  "MCMXCIV"
    to_roman(58)            ->  "LVIII"
    to_roman(3999)          ->  "MMMCMXCIX"
    from_roman("MCMXCIV")   ->  1994
    from_roman("IV")        ->  4
    from_roman("ABC")       ->  ValueError

Contraintes
    - règles habituelles (pas de listes ni de dictionnaires !)

Indice
    to_roman : chaque chiffre décimal s'écrit avec le MÊME schéma, seules
    les lettres changent :
        unités    : (un, cinq, dix) = ("I", "V", "X")
        dizaines  : ("X", "L", "C")
        centaines : ("C", "D", "M")
    Un helper _digit(d, one, five, ten) qui gère d = 0..9 fait tout le
    travail (4 cas : 0-3, 4, 5-8, 9). Les milliers : juste des "M".
    from_roman : lis de gauche à droite ; si la valeur du symbole courant
    est plus petite que celle du SUIVANT, on la soustrait, sinon on l'ajoute.

Vérifier : python3 check.py roman
"""


def to_roman(n: int) -> str:
    pass


def from_roman(s: str) -> int:
    pass


if __name__ == "__main__":
    print(to_roman(1994), from_roman("MCMXCIV"))
