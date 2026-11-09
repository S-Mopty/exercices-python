"""
predict — Niveau 4 ★★   « Joue l'ordinateur »

Pas de code à écrire ici. Tu dois PRÉDIRE ce que font les fonctions
mystère ci-dessous, SANS les exécuter. Prends une feuille, dessine l'arbre
des appels (voir la fiche du niveau 4), et remplis les PREDICTION_... en
bas du fichier.

    - Pour un affichage : écris les valeurs affichées, séparées par des
      espaces. Si la fonction affiche 1, puis 2, puis 3 (une par ligne),
      écris "1 2 3".
    - Pour une valeur renvoyée : écris un int (8, pas "8").

Le correcteur te dit lesquelles sont justes, sans te donner la réponse.
Ne lance pas le fichier pour tricher : le but est d'entraîner TA tête.
C'est exactement la compétence qui manque quand Hanoï « ne rentre pas ».

Vérifier : python3 check.py predict
"""


def mystery_a(n):
    if n == 0:
        return
    mystery_a(n - 1)
    print(n)
    mystery_a(n - 1)


def mystery_b(n):
    if n >= 10:
        mystery_b(n // 10)
    print(n % 10)


def mystery_c(n):
    if n <= 1:
        return 1
    return mystery_c(n - 1) + mystery_c(n - 2)


def mystery_d(n, x, y):
    if n > 0:
        mystery_d(n - 1, y, x)
        print(x + y)
        mystery_d(n - 1, y, x)


def mystery_e(n):
    if n == 0:
        return 0
    print(n)
    r = mystery_e(n - 1)
    print(r)
    return r + n


# Q1. Qu'affiche mystery_a(3) ?
PREDICTION_1 = None

# Q2. Qu'affiche mystery_b(907) ?
PREDICTION_2 = None

# Q3. Que RENVOIE mystery_c(5) ?
PREDICTION_3 = None

# Q4. Pour calculer mystery_c(5), combien d'appels à mystery_c sont faits
#     au total (l'appel mystery_c(5) lui-même compte) ?
PREDICTION_4 = None

# Q5. Qu'affiche mystery_d(2, "A", "B") ?
PREDICTION_5 = None

# Q6. Qu'affiche mystery_d(3, "A", "B") ?
PREDICTION_6 = None

# Q7. Qu'affiche mystery_e(3) ?
PREDICTION_7 = None

# Q8. Que RENVOIE mystery_e(3) ?
PREDICTION_8 = None
