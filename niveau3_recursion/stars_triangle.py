"""
stars_triangle — Niveau 3 ★★★

Écris une fonction RÉCURSIVE `stars_triangle(n)` qui affiche un triangle de
n lignes : la ligne k contient k étoiles. Elle RENVOIE le nombre total
d'étoiles affichées. Si n <= 0 : n'affiche rien et renvoie 0.

Exemple
    print(stars_triangle(4))
Sortie
    *
    **
    ***
    ****
    10

Contraintes
    - récursif de bout en bout : aucune boucle, même pour une ligne
    - "*" * k interdit

Indice
    Deux fonctions récursives qui coopèrent :
      - _stars(k) RENVOIE (sans afficher) une chaîne de k étoiles ;
      - stars_triangle(n) dessine le triangle de taille n - 1, PUIS affiche
        sa propre ligne de n étoiles (même idée que count_up).
    total(n) = total(n - 1) + n.

Vérifier : python3 check.py stars_triangle
"""


def stars_triangle(n: int) -> int:
    pass


if __name__ == "__main__":
    print(stars_triangle(4))
