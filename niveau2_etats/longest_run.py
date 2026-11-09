"""
longest_run — Niveau 2 ★★

Écris `longest_run(text)` qui renvoie la longueur de la plus longue suite
de caractères identiques consécutifs dans `text`.

Exemples
    longest_run("aabbbbcdd")  ->  4      (les quatre 'b')
    longest_run("abc")        ->  1
    longest_run("aabba")      ->  2
    longest_run("")           ->  0

Contraintes
    - boucle obligatoire ; max() interdit

Indice
    Pattern « meilleur jusqu'ici » : une variable pour la suite EN COURS,
    une autre pour la MEILLEURE vue depuis le début. À chaque tour, mets à
    jour la première, puis compare-la à la seconde.

Vérifier : python3 check.py longest_run
"""


def longest_run(text: str) -> int:
    pass


if __name__ == "__main__":
    print(longest_run("aabbbbcdd"))
