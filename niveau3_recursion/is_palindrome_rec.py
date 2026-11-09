"""
is_palindrome_rec — Niveau 3 ★★★

Écris une fonction RÉCURSIVE `is_palindrome_rec(text)` qui renvoie True si
`text` se lit pareil dans les deux sens EN IGNORANT LES ESPACES, False
sinon. La casse compte ('K' != 'k'). Le texte vide est un palindrome.

Exemples
    is_palindrome_rec("kayak")              ->  True
    is_palindrome_rec("never odd or even")  ->  True
    is_palindrome_rec("taco cat")           ->  True
    is_palindrome_rec("Kayak")              ->  False
    is_palindrome_rec("abca")               ->  False
    is_palindrome_rec("   ")                ->  True

Contraintes
    - récursive, aucune boucle, pas de slicing

Indice
    Helper _check(text, left, right) avec deux indices qui se rapprochent.
      - left >= right : plus rien à comparer -> True
      - text[left] est un espace : on le saute -> _check(text, left + 1, right)
      - text[right] est un espace : pareil de l'autre côté
      - sinon : compare text[left] et text[right] ; s'ils sont égaux,
        continue avec les indices suivants.

Vérifier : python3 check.py is_palindrome_rec
"""


def is_palindrome_rec(text: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_palindrome_rec("never odd or even"))
