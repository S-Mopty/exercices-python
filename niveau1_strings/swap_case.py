"""
swap_case — Niveau 1 ★

Écris `swap_case(text)` qui renvoie `text` où chaque majuscule devient
minuscule et chaque minuscule devient majuscule. Les autres caractères
(chiffres, espaces, ponctuation) ne changent pas.

Exemples
    swap_case("Hello World 42")  ->  "hELLO wORLD 42"
    swap_case("PyThOn")          ->  "pYtHoN"
    swap_case("123 !?")          ->  "123 !?"

Contraintes
    - boucle obligatoire
    - pas de .swapcase(), .lower(), .upper() : passe par ord() / chr()

Indice
    Trois cas pour chaque caractère : majuscule ('A'..'Z'), minuscule
    ('a'..'z'), ou autre. Un if / elif / else suffit.
    Rappel : chr(ord(c) - ord('A') + ord('a')) transforme 'C' en 'c'.

Vérifier : python3 check.py swap_case
"""


def swap_case(text: str) -> str:
    pass


if __name__ == "__main__":
    print(swap_case("Hello World 42"))
