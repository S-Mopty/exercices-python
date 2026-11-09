"""
binary_words — Niveau 4 ★★★

Écris une fonction RÉCURSIVE `binary_words(n)` qui affiche tous les mots
binaires (faits de '0' et de '1') de longueur n, dans l'ordre croissant,
un par ligne, et RENVOIE le nombre de mots affichés.
    - n == 0 : il existe exactement un mot de longueur 0, le mot vide.
      La fonction affiche donc une ligne vide et renvoie 1.
    - n < 0 : lever ValueError.

Exemple
    print(binary_words(3))
Sortie
    000
    001
    010
    011
    100
    101
    110
    111
    8

Contraintes
    - récursive, aucune boucle
    - ** interdit (le compte doit remonter des appels)

Indice
    Helper _gen(prefix, remaining) : « affiche tous les mots qui commencent
    par prefix et auxquels il manque encore `remaining` caractères ».
      - remaining == 0 : le mot est complet -> l'afficher, renvoyer 1
      - sinon : TOUS les mots qui continuent par "0", PUIS tous ceux qui
        continuent par "1". Renvoyer la somme des deux comptes.
    Le paramètre `prefix` accumule le chemin parcouru dans l'arbre.

Vérifier : python3 check.py binary_words
"""


def binary_words(n: int) -> int:
    pass


if __name__ == "__main__":
    print(binary_words(3))
