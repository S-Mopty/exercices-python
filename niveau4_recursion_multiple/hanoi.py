"""
hanoi — Niveau 4 ★★★★   (le boss du niveau)

Les tours de Hanoï : n disques empilés sur la tour `src`, du plus grand
(disque n, en bas) au plus petit (disque 1, en haut). Il faut tous les
amener sur la tour `dst`, en s'aidant de la tour `aux`.
    - on déplace un seul disque à la fois (celui du dessus d'une tour) ;
    - jamais un disque sur un disque plus petit.

Écris une fonction RÉCURSIVE `hanoi(n, src, aux, dst)` qui affiche chaque
déplacement sous la forme
    disk K: X -> Y
(K = numéro du disque déplacé, X et Y = noms des tours) et qui RENVOIE le
nombre de déplacements.
    - n == 0 : rien à faire, renvoie 0.
    - n < 0 : lever ValueError("Invalid disk count").

Exemple
    print(hanoi(2, "A", "B", "C"))
Sortie
    disk 1: A -> B
    disk 2: A -> C
    disk 1: B -> C
    3

Exemple
    print(hanoi(3, "L", "M", "R"))
Sortie
    disk 1: L -> R
    disk 2: L -> M
    disk 1: R -> M
    disk 3: L -> R
    disk 1: M -> L
    disk 2: M -> R
    disk 1: L -> R
    7

Contraintes
    - récursive, aucune boucle
    - ** interdit : le compte doit venir des appels (pas de 2 ** n - 1)

Indice (lis d'abord la fiche du niveau 4)
    Pour déplacer n disques de src vers dst :
      1. déplacer les n - 1 disques du dessus de src vers aux
         (en utilisant dst comme tour intermédiaire) ;
      2. déplacer le disque n de src vers dst ;
      3. déplacer les n - 1 disques de aux vers dst
         (en utilisant src comme tour intermédiaire).
    Ne « déroule » PAS les appels dans ta tête : fais confiance à l'étape 1
    comme si elle marchait déjà. C'est tout le principe de la récursion.
    Et compare avec ruler : même squelette, à un détail près (les rôles
    des tours changent d'un appel à l'autre).

Vérifier : python3 check.py hanoi
"""


def hanoi(n: int, src: str, aux: str, dst: str) -> int:
    pass


if __name__ == "__main__":
    print(hanoi(3, "A", "B", "C"))
