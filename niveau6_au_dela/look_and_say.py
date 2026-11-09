"""
look_and_say — Niveau 6 ★★★

La suite « look and say » (« lis ce que tu vois ») : chaque terme décrit
le précédent à voix haute.
    1          -> « un 1 »                    -> 11
    11         -> « deux 1 »                  -> 21
    21         -> « un 2, un 1 »              -> 1211
    1211       -> « un 1, un 2, deux 1 »      -> 111221
    111221     -> « trois 1, deux 2, un 1 »   -> 312211

Écris `look_and_say(n)` qui renvoie le n-ième terme (le 1er terme est "1").
Si n < 1 : lever ValueError.

Exemples
    look_and_say(1)   ->  "1"
    look_and_say(4)   ->  "1211"
    look_and_say(6)   ->  "312211"
    look_and_say(10)  ->  "13211311123113112211"

Contraintes
    - boucles obligatoires ; str() autorisé

Indice
    Écris d'abord un helper describe(term) qui passe d'un terme au
    suivant : c'est ton compress du niveau 2, avec le nombre AVANT le
    chiffre. Ensuite, look_and_say applique describe n - 1 fois.
    Réutiliser un exercice précédent, c'est exactement ce qu'on attend.

Vérifier : python3 check.py look_and_say
"""


def look_and_say(n: int) -> str:
    pass


if __name__ == "__main__":
    print(look_and_say(6))
