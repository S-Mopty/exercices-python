"""
find_sub — Niveau 2 ★★★

Écris `find_sub(text, pattern)` qui renvoie l'indice de la première
occurrence de la chaîne `pattern` dans `text`, ou -1 si elle n'y est pas.
Une chaîne vide est trouvée à l'indice 0.

Exemples
    find_sub("hello", "ll")             ->  2
    find_sub("aaab", "ab")              ->  2
    find_sub("mississippi", "issip")    ->  4
    find_sub("abc", "abcd")             ->  -1
    find_sub("abc", "")                 ->  0

Contraintes
    - boucles obligatoires
    - interdits : .find(), slicing, et `pattern in text`

Indice
    Deux boucles imbriquées. Pour chaque position de départ i possible
    dans text, compare pattern caractère par caractère avec text[i + j].
    Combien de positions de départ possibles ? len(text) - len(pattern) + 1
    (et si c'est <= 0, aucune). Un booléen `match` qui passe à False dès
    qu'un caractère diffère.
    Piège : "aaab" / "ab". Si ta version renvoie -1, c'est qu'après un
    échec tu n'as pas recommencé à la bonne position.

Vérifier : python3 check.py find_sub
"""


def find_sub(text: str, pattern: str) -> int:
    pass


if __name__ == "__main__":
    print(find_sub("mississippi", "issip"))
