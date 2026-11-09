"""
is_number — Niveau 1 ★★

Écris `is_number(text)` qui renvoie True si `text` représente un nombre
entier, False sinon. Un nombre entier, c'est :
    - au moins un chiffre,
    - uniquement des chiffres,
    - avec éventuellement UN signe '-' tout au début.

Exemples
    is_number("42")    ->  True
    is_number("-42")   ->  True
    is_number("007")   ->  True
    is_number("4-2")   ->  False
    is_number("-")     ->  False
    is_number("")      ->  False
    is_number("+3")    ->  False
    is_number("--1")   ->  False

Contraintes
    - boucle obligatoire
    - doit renvoyer un vrai booléen (True / False), pas 1 / 0 ni "True"

Indice
    Le premier caractère est un cas particulier : c'est le seul qui a le
    droit d'être un '-'. Utilise une variable `start` (0 ou 1) qui dit à
    partir de quel indice tous les caractères doivent être des chiffres.
    Et n'oublie pas le cas où il n'y a AUCUN chiffre.

Vérifier : python3 check.py is_number
"""


def is_number(text: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_number("-42"))
