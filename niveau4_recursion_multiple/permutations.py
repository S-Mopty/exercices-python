"""
permutations — Niveau 4 ★★★★   (récursion + boucle)

Écris `permutations(text)` qui affiche toutes les permutations des
caractères de `text` (tous distincts), une par ligne, et RENVOIE leur
nombre. L'ordre est imposé : on choisit d'abord le 1er caractère disponible,
puis le 2e, etc. (voir l'exemple). Pour text = "", on affiche une ligne
vide et on renvoie 1.

Exemple
    print(permutations("abc"))
Sortie
    abc
    acb
    bac
    bca
    cab
    cba
    6

Contraintes
    - récursive ; les boucles sont autorisées (et utiles !)
    - pas de listes, pas de slicing

Indice
    Helper _perm(prefix, rest) : « affiche toutes les permutations qui
    commencent par prefix, en utilisant les caractères de rest ».
      - rest vide : afficher prefix, renvoyer 1
      - sinon : pour chaque indice i de rest, choisir rest[i] :
            _perm(prefix + rest[i], rest privé de son caractère i)
        et additionner les comptes.
    « rest privé de son caractère i » : écris un helper _without(s, i)
    avec une boucle (le slicing est interdit).
    Différence avec binary_words : ici le nombre de branches n'est pas
    fixe (2), il dépend de len(rest). D'où la boucle.

Vérifier : python3 check.py permutations
"""


def permutations(text: str) -> int:
    pass


if __name__ == "__main__":
    print(permutations("abc"))
