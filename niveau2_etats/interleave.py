"""
interleave — Niveau 2 ★★

Écris `interleave(a, b)` qui entrelace les caractères de `a` et `b` :
a[0], b[0], a[1], b[1], ... Quand une des deux chaînes est épuisée, on
ajoute la fin de l'autre.

Exemples
    interleave("abc", "12345")  ->  "a1b2c345"
    interleave("abcd", "12")    ->  "a1b2cd"
    interleave("", "xy")        ->  "xy"
    interleave("", "")          ->  ""

Contraintes
    - boucle obligatoire ; max() et le slicing sont interdits

Indice
    Calcule toi-même la plus grande des deux longueurs (un if suffit),
    puis boucle sur i de 0 à cette longueur. À chaque tour : ajoute a[i]
    SI i est un indice valide de a, puis b[i] si i est valide pour b.

Vérifier : python3 check.py interleave
"""


def interleave(a: str, b: str) -> str:
    pass


if __name__ == "__main__":
    print(interleave("abc", "12345"))
