"""
n_queens — Niveau 6 ★★★★★   (le boss final)

Sur un échiquier n x n, de combien de façons peut-on placer n reines sans
qu'aucune n'en attaque une autre ? (Une reine attaque sur sa ligne, sa
colonne et ses deux diagonales.)
Écris `n_queens(n)` qui renvoie ce nombre, pour 0 <= n <= 9.
Sinon : lever ValueError. Par convention, n_queens(0) vaut 1.

Exemples
    n_queens(1)  ->  1
    n_queens(2)  ->  0
    n_queens(4)  ->  2
    n_queens(6)  ->  4
    n_queens(8)  ->  92

Contraintes
    - récursive (backtracking), pas de listes ; abs() interdit

Indice
    Une reine par ligne, forcément. On pose les reines ligne après ligne.
    État = une chaîne `placed` de chiffres : placed[r] est la colonne de la
    reine posée sur la ligne r. Par exemple "13" : reine en colonne 1 sur
    la ligne 0, en colonne 3 sur la ligne 1.
        _solve(n, placed) :
            si len(placed) == n : une solution complète -> 1
            sinon, pour chaque colonne c de 0 à n - 1 :
                si c est sûre vis-à-vis de toutes les reines de placed,
                    ajouter _solve(n, placed + chr(c + ord('0')))
    « Sûre » (helper _safe) : pour chaque reine déjà posée (ligne r,
    colonne qc), même colonne si qc == c ; même diagonale si la distance
    entre les lignes égale la distance entre les colonnes. Écris ton
    propre helper de valeur absolue.
    C'est le schéma de permutations (une boucle de choix + un appel
    récursif), avec en plus un test qui coupe les branches impossibles.

Vérifier : python3 check.py n_queens
"""


def n_queens(n: int) -> int:
    pass


if __name__ == "__main__":
    print(n_queens(8))
