"""
alternate_case — Niveau 2 ★★

Écris `alternate_case(text)` qui renvoie `text` où les LETTRES alternent
majuscule / minuscule, en commençant par une majuscule. Les autres
caractères (espaces, chiffres, ponctuation) sont recopiés tels quels et ne
comptent PAS dans l'alternance.

Exemples
    alternate_case("hello world")  ->  "HeLlO wOrLd"
    alternate_case("a-b-c")        ->  "A-b-C"
    alternate_case("PYTHON")       ->  "PyThOn"
    alternate_case("123")          ->  "123"

    Détail de "hello world" : h e l l o _ w o r l d
                     n° lettre : 0 1 2 3 4   5 6 7 8 9
          (pair -> MAJ, impair -> min ; l'espace n'a pas de numéro)

Contraintes
    - boucle obligatoire, ord() / chr() pour changer la casse

Indice
    Il te faut un compteur `letter_index` À CÔTÉ de la boucle, qui n'avance
    QUE quand le caractère est une lettre. La boucle, elle, avance sur tous
    les caractères. Deux « vitesses » différentes : c'est exactement la
    mécanique de la clé dans un chiffrement de Vigenère.

Vérifier : python3 check.py alternate_case
"""


def alternate_case(text: str) -> str:
    pass


if __name__ == "__main__":
    print(alternate_case("hello world"))
