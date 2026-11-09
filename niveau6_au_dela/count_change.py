"""
count_change — Niveau 6 ★★★★

De combien de façons peut-on payer la somme `amount` avec des pièces dont
les valeurs sont les chiffres de la chaîne `coins` ? Chaque pièce est
disponible en quantité illimitée, et l'ordre ne compte pas (1+2 et 2+1,
c'est la même façon). Les chiffres de `coins` sont distincts, entre 1 et 9.
Écris la fonction RÉCURSIVE `count_change(amount, coins)`.
Si amount < 0 : lever ValueError.

Exemples
    count_change(4, "12")     ->  3     (1+1+1+1, 1+1+2, 2+2)
    count_change(10, "125")   ->  10
    count_change(3, "2")      ->  0
    count_change(0, "5")      ->  1     (une seule façon : ne rien donner)
    count_change(7, "")       ->  0

Contraintes
    - récursive

Indice
    Le grand classique de la récursion à deux branches. Regarde la pièce
    d'indice i. Soit tu l'utilises (au moins) une fois de plus, soit tu
    décides de ne plus JAMAIS l'utiliser :
        ways(amount, i) = ways(amount - pièce_i, i) + ways(amount, i + 1)
    Cas de base : amount == 0 -> 1 façon ; amount < 0 -> 0 ;
    plus de pièces (i == len(coins)) -> 0.
    Pourquoi pas « pour chaque pièce, ways(amount - pièce) » ? Essaie :
    tu compteras 1+2 et 2+1 séparément.

Vérifier : python3 check.py count_change
"""


def count_change(amount: int, coins: str) -> int:
    pass


if __name__ == "__main__":
    print(count_change(10, "125"))
