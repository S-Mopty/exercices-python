"""
count_up — Niveau 3 ★

Écris une fonction RÉCURSIVE `count_up(n)` qui affiche les entiers de 1 à
n, un par ligne, DANS L'ORDRE CROISSANT. Elle ne renvoie rien.
Si n <= 0, elle n'affiche rien.

Exemple
    count_up(3)
Sortie
    1
    2
    3

Contraintes
    - récursive, aucune boucle
    - pas de deuxième paramètre (pas de count_up(n, i))

Indice
    Tu sais sans doute écrire le compte à rebours n, n-1, ..., 1 : on
    affiche n, PUIS on fait l'appel récursif. Ici, inverse les deux lignes.
    Pourquoi ça marche ? count_up(3) attend que count_up(2) ait FINI
    (donc affiché 1 et 2) avant d'afficher 3.
    -> Ce qui est écrit APRÈS l'appel récursif s'exécute « au retour »,
       dans l'ordre inverse des appels. Retiens-le : c'est la clé de Hanoï.

Vérifier : python3 check.py count_up
"""


def count_up(n: int) -> None:
    pass


if __name__ == "__main__":
    count_up(3)
