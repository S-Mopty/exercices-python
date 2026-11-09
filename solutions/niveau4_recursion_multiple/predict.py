"""Solution — predict (niveau 4).

Lance ce fichier (python3 solutions/niveau4_recursion_multiple/predict.py)
pour voir les vraies sorties, APRÈS avoir fait tes prédictions.
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


# Q1. mystery_a(3) : même forme que ruler. a(2) affiche "1 2 1", donc
#     a(3) = a(2), 3, a(2).
PREDICTION_1 = "1 2 1 3 1 2 1"

# Q2. Les chiffres sont affichés « au retour » : de gauche à droite.
PREDICTION_2 = "9 0 7"

# Q3. c(0) = c(1) = 1, c(2) = 2, c(3) = 3, c(4) = 5, c(5) = 8.
PREDICTION_3 = 8

# Q4. appels(n) = 1 + appels(n-1) + appels(n-2), appels(0) = appels(1) = 1
#     -> 1, 1, 3, 5, 9, 15.
PREDICTION_4 = 15

# Q5. d(2, A, B) = d(1, B, A), "AB", d(1, B, A) ; et d(1, B, A) affiche "BA".
PREDICTION_5 = "BA AB BA"

# Q6. d(3, A, B) = d(2, B, A), "AB", d(2, B, A) ;
#     d(2, B, A) = d(1, A, B), "BA", d(1, A, B) = "AB BA AB".
PREDICTION_6 = "AB BA AB AB AB BA AB"

# Q7. À l'aller : 3 2 1. Au retour, chaque niveau affiche ce que l'appel
#     du dessous a renvoyé : e(0) -> 0, e(1) -> 1, e(2) -> 3.
PREDICTION_7 = "3 2 1 0 1 3"

# Q8. e(3) = e(2) + 3 = 3 + 3.
PREDICTION_8 = 6


if __name__ == "__main__":
    for label, call in [("Q1", lambda: mystery_a(3)), ("Q2", lambda: mystery_b(907)),
                        ("Q5", lambda: mystery_d(2, "A", "B")),
                        ("Q6", lambda: mystery_d(3, "A", "B")),
                        ("Q7", lambda: mystery_e(3))]:
        print("---", label)
        call()
