"""
add_big — Niveau 6 ★★★

Écris `add_big(a, b)` qui additionne deux nombres positifs donnés sous
forme de chaînes de chiffres, de longueur quelconque, et renvoie la somme
sous forme de chaîne. Exactement comme l'addition posée de l'école.
Les entrées n'ont pas de zéros inutiles devant (sauf "0" lui-même).
Lever ValueError si a ou b est vide ou contient autre chose que des chiffres.

Exemples
    add_big("123", "989")                    ->  "1112"
    add_big("0", "0")                        ->  "0"
    add_big("99999999999999999999", "1")     ->  "100000000000000000000"
    add_big("1", "999")                      ->  "1000"

Contraintes
    - boucle obligatoire
    - int() ET str() interdits : en Python, int() gère des entiers géants
      et rendrait l'exercice trivial. Un chiffre <-> sa valeur : ord / chr.

Indice
    Deux indices i et j qui partent de la FIN de a et de b, et une retenue
    `carry`. À chaque tour :
        somme = chiffre(a, i) + chiffre(b, j) + carry   (0 si épuisé)
        on écrit somme % 10 DEVANT le résultat, carry = somme // 10
    On continue tant qu'il reste des chiffres d'un côté OU une retenue.

Vérifier : python3 check.py add_big
"""


def add_big(a: str, b: str) -> str:
    pass


if __name__ == "__main__":
    print(add_big("99999999999999999999", "1"))
