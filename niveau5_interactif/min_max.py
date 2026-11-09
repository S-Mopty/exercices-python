"""
min_max — Niveau 5 ★★★

Écris `min_max()` qui lit d'abord un entier n (prompt "how many? "), puis
n entiers (prompt "> " pour chacun), et affiche le plus petit et le plus
grand sur deux lignes : "min: A" puis "max: B".
Si n <= 0 : afficher "nothing to do" (et ne rien lire d'autre).
La fonction ne renvoie rien.

Exemple
    how many? 4
    > 7
    > -3
    > 12
    > 0
    min: -3
    max: 12

Contraintes
    - boucle obligatoire
    - min(), max() et les listes sont interdits : tu ne peux PAS stocker
      les nombres, il faut tout faire « au vol »

Indice
    Initialiser min et max à 0 est faux. Pourquoi ? (essaie avec 5, 8, 9)
    Initialise-les avec le PREMIER nombre lu, puis compare les suivants.

Vérifier : python3 check.py min_max
"""


def min_max() -> None:
    pass


if __name__ == "__main__":
    min_max()
