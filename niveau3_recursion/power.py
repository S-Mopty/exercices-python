"""
power — Niveau 3 ★

Écris une fonction RÉCURSIVE `power(x, n)` qui renvoie x puissance n,
pour n >= 0. Si n < 0 : lever ValueError.

Exemples
    power(2, 10)  ->  1024
    power(5, 0)   ->  1
    power(-3, 3)  ->  -27

Contraintes
    - récursive, aucune boucle
    - `**` interdit

Indice
    Les 3 questions à se poser pour TOUTE fonction récursive :
      1. Cas de base : pour quel n je connais la réponse sans réfléchir ?
      2. Cas récursif : si quelqu'un me donne power(x, n - 1), comment
         j'obtiens power(x, n) ?
      3. Est-ce que chaque appel se rapproche du cas de base ?

Bonus (non testé) : x^n = (x^(n//2))^2 quand n est pair. Écris une
version qui fait beaucoup moins d'appels (« puissance rapide »).

Vérifier : python3 check.py power
"""


def power(x: int, n: int) -> int:
    pass


if __name__ == "__main__":
    print(power(2, 10))
