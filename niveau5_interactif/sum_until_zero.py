"""
sum_until_zero — Niveau 5 ★★

Écris `sum_until_zero()` qui lit des entiers (prompt "number: ") jusqu'à ce
que l'utilisateur tape 0. Elle affiche alors "total: T (K numbers)" où T est
la somme et K le nombre d'entiers lus (le 0 final ne compte pas), et
RENVOIE T.

Exemple
    number: 5
    number: -2
    number: 10
    number: 0
    total: 13 (3 numbers)

Contraintes
    - boucle while obligatoire
    - input() renvoie TOUJOURS une chaîne : convertis avec int()
    - les entrées sont toujours des entiers valides

Indice
    Piège classique : faire `total = total + input(...)`. Python refuse
    d'additionner un int et une str, et "5" + "3" donnerait "53".

Vérifier : python3 check.py sum_until_zero
"""


def sum_until_zero() -> int:
    pass


if __name__ == "__main__":
    print(sum_until_zero())
