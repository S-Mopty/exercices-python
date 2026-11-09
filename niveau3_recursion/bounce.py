"""
bounce — Niveau 3 ★★

Écris une fonction RÉCURSIVE `bounce(n)` qui affiche n, n-1, ..., 1 puis
1, 2, ..., n (un nombre par ligne), et qui RENVOIE le nombre de lignes
affichées. Si n <= 0 : n'affiche rien et renvoie 0.

Exemple
    print(bounce(3))
Sortie
    3
    2
    1
    1
    2
    3
    6

Contraintes
    - récursive, aucune boucle
    - le nombre de lignes doit « remonter » des appels récursifs : ne
      renvoie pas simplement 2 * n

Indice
    Un print AVANT l'appel récursif, un print APRÈS. Et pour le compte :
    lignes(n) = lignes(n - 1) + 2. Récupère la valeur renvoyée par l'appel
    récursif dans une variable, ajoute ce que TOI tu as affiché, renvoie.
    -> C'est exactement comme ça que Hanoï compte ses déplacements.

Vérifier : python3 check.py bounce
"""


def bounce(n: int) -> int:
    pass


if __name__ == "__main__":
    print(bounce(3))
