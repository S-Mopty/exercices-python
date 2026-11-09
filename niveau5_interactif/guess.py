"""
guess — Niveau 5 ★★

Écris `guess(secret)` : un jeu du « plus ou moins ». En boucle, la fonction
lit un entier (prompt "guess: ") et affiche :
    - "too low"   si la proposition est plus petite que secret ;
    - "too high"  si elle est plus grande ;
    - "found in K tries!" si c'est le bon nombre (K = nombre d'essais),
      ou "found in 1 try!" si trouvé du premier coup. Puis elle RENVOIE K.

Exemple
    guess(37)
Sortie
    guess: 50
    too high
    guess: 25
    too low
    guess: 37
    found in 3 tries!

Contraintes
    - boucle while obligatoire

Vérifier : python3 check.py guess
"""


def guess(secret: int) -> int:
    pass


if __name__ == "__main__":
    print(guess(37))
