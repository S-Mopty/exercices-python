"""
grid_paths — Niveau 4 ★★★

Tu es dans le coin en haut à gauche d'une grille. Tu dois faire exactement
`rows` pas vers le bas et `cols` pas vers la droite, dans n'importe quel
ordre. Écris une fonction RÉCURSIVE `grid_paths(rows, cols)` qui renvoie le
nombre de chemins différents possibles.
Si rows ou cols est négatif : lever ValueError.

Exemples
    grid_paths(2, 2)  ->  6     (BBDD, BDBD, BDDB, DBBD, DBDB, DDBB)
    grid_paths(1, 3)  ->  4
    grid_paths(0, 5)  ->  1     (tout droit)
    grid_paths(3, 3)  ->  20

Contraintes
    - récursive, aucune boucle

Indice
    Ton DERNIER pas est soit vers le bas, soit vers la droite. Donc :
        chemins(r, c) = chemins(r - 1, c) + chemins(r, c - 1)
    Deux appels récursifs, on additionne leurs résultats. Quel est le cas
    de base ? (S'il ne reste qu'une direction, combien de chemins ?)
    Bonus (non testé) : grid_paths(15, 15) est très lent. Pourquoi ?
    Compte les appels (même idée que fibo_calls).

Vérifier : python3 check.py grid_paths
"""


def grid_paths(rows: int, cols: int) -> int:
    pass


if __name__ == "__main__":
    print(grid_paths(2, 2))
