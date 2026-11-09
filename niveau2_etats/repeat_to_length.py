"""
repeat_to_length — Niveau 2 ★★

Écris `repeat_to_length(pattern, n)` qui renvoie une chaîne de longueur
exactement `n`, obtenue en répétant `pattern` autant que nécessaire (la
dernière répétition peut être coupée).

Si `pattern` est vide ou si `n` est négatif : lever ValueError.

Exemples
    repeat_to_length("abc", 7)  ->  "abcabca"
    repeat_to_length("ab", 4)   ->  "abab"
    repeat_to_length("xyz", 0)  ->  ""
    repeat_to_length("", 3)     ->  ValueError

Contraintes
    - boucle obligatoire
    - raise ValueError("Invalid argument") pour les cas invalides

Indice
    Le caractère n° i du résultat est pattern[i % len(pattern)].
    Le modulo « fait boucler » un indice sur une chaîne plus courte : c'est
    LA formule à retenir pour toutes les clés qui se répètent.

Vérifier : python3 check.py repeat_to_length
"""


def repeat_to_length(pattern: str, n: int) -> str:
    pass


if __name__ == "__main__":
    print(repeat_to_length("abc", 7))
