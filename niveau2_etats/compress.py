"""
compress — Niveau 2 ★★

Écris `compress(text)` qui « compresse » `text` : chaque suite de
caractères identiques consécutifs est remplacée par ce caractère suivi du
nombre de répétitions.

Exemples
    compress("aaabccdddd")     ->  "a3b1c2d4"
    compress("abc")            ->  "a1b1c1"
    compress("zzzzzzzzzzzz")   ->  "z12"
    compress("aabbaa")         ->  "a2b2a2"
    compress("")               ->  ""

Contraintes
    - boucle obligatoire ; str() autorisé pour écrire le nombre

Indice
    Deux variables d'état : le caractère du bloc en cours, et sa longueur.
    Quand le caractère change, le bloc précédent est terminé : écris-le
    dans le résultat, puis démarre un nouveau bloc.
    Piège classique : le DERNIER bloc n'est suivi d'aucun changement, donc
    la boucle ne l'écrit jamais. Il faut le traiter après la boucle.

Vérifier : python3 check.py compress
"""


def compress(text: str) -> str:
    pass


if __name__ == "__main__":
    print(compress("aaabccdddd"))
