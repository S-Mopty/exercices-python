"""
digit_cipher — Niveau 2 ★★★  (deux fonctions dans ce fichier)

Un chiffrement à clé numérique. La clé `key` est une chaîne de chiffres,
par exemple "314". Chaque LETTRE du message est décalée dans l'alphabet du
chiffre suivant de la clé : la 1re lettre de 3, la 2e de 1, la 3e de 4, la
4e de nouveau de 3, etc. (la clé se répète).

Règles :
    - la casse est conservée, l'alphabet boucle (z + 1 -> a, Z + 1 -> A) ;
    - les caractères qui ne sont pas des lettres sont recopiés tels quels
      et NE CONSOMMENT PAS de chiffre de la clé ;
    - si `key` est vide : lever ValueError.

1) `digit_shift(text, key)` chiffre (décalage vers l'avant).
2) `digit_unshift(text, key)` déchiffre (décalage vers l'arrière) :
   digit_unshift(digit_shift(t, k), k) doit redonner t.

Exemples
    digit_shift("abc", "12")         ->  "bdd"     (a+1, b+2, c+1)
    digit_shift("Hi, Bob!", "314")   ->  "Kj, Frc!"
    digit_shift("zZ", "1")           ->  "aA"
    digit_unshift("Kj, Frc!", "314") ->  "Hi, Bob!"

    Détail de "Hi, Bob!" avec "314" :
        H  i  ,  _  B  o  b  !
        3  1  .  .  4  3  1  .      ('.' = pas une lettre, la clé n'avance pas)

Contraintes
    - boucle obligatoire, ord() / chr() ; tu peux écrire des helpers

Indice
    Même mécanique qu'alternate_case : un index de clé `k` qui n'avance QUE
    sur les lettres. Le décalage courant vaut ord(key[k % len(key)]) - ord('0').
    Écris un helper shift_letter(c, d) qui décale UNE lettre de d (d peut
    être négatif : en Python, (-3) % 26 vaut 23, le modulo gère tout).
    -> Si tu réussis ça, le Vigenère du TP n'a plus de secret : c'est la
       même chose avec des lettres à la place des chiffres.

Vérifier : python3 check.py digit_cipher
"""


def digit_shift(text: str, key: str) -> str:
    pass


def digit_unshift(text: str, key: str) -> str:
    pass


if __name__ == "__main__":
    print(digit_shift("Hi, Bob!", "314"))
