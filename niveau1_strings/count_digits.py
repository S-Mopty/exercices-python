"""
count_digits — Niveau 1 ★

Écris `count_digits(text)` qui renvoie le nombre de chiffres ('0' à '9')
présents dans `text`.

Exemples
    count_digits("R2-D2 et C-3PO")  ->  3
    count_digits("2026")            ->  4
    count_digits("")                ->  0

Contraintes
    - boucle obligatoire
    - aucune méthode de str (donc pas de .isdigit())

Indice (seulement si tu bloques plus de 10 min)
    Les caractères '0'..'9' ont des codes ord() consécutifs. Pas besoin de
    les apprendre par cœur : ord('0') <= ord(c) <= ord('9').

Vérifier : python3 check.py count_digits
"""


def count_digits(text: str) -> int:
    pass


if __name__ == "__main__":
    # Tes tests perso ici : ils ne gênent pas le correcteur.
    print(count_digits("R2-D2 et C-3PO"))
