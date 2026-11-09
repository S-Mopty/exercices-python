"""
count_digit — Niveau 3 ★★

Écris une fonction RÉCURSIVE `count_digit(n, d)` qui renvoie le nombre de
fois où le chiffre `d` (0 à 9) apparaît dans l'entier `n` (n >= 0).

Exemples
    count_digit(1231, 1)   ->  2
    count_digit(1000, 0)   ->  3
    count_digit(0, 0)      ->  1      (le nombre 0 s'écrit avec un chiffre 0)
    count_digit(7, 3)      ->  0

Contraintes
    - récursive, aucune boucle
    - str() interdit : on travaille sur le nombre, pas sur son texte

Indice
    n % 10 donne le dernier chiffre, n // 10 enlève le dernier chiffre.
    Attention au cas de base : si tu t'arrêtes à « n == 0 », alors
    count_digit(0, 0) renvoie 0 au lieu de 1 (vérifie à la main).
    Arrête-toi plutôt quand il ne reste qu'UN chiffre (n < 10).

Vérifier : python3 check.py count_digit
"""


def count_digit(n: int, d: int) -> int:
    pass


if __name__ == "__main__":
    print(count_digit(1231, 1))
