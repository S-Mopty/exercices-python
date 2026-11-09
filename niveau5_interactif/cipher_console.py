"""
cipher_console — Niveau 5 ★★★★   (le boss : tout le bloc 1 en un programme)

Écris `cipher_console()`, une petite console de chiffrement de César.

Au démarrage, elle affiche UNE fois :
    == CIPHER CONSOLE ==
    1) encode  2) decode  3) quit
Puis, en boucle, elle lit un choix (prompt "choice: ") :
    - "1" : lit un texte (prompt "text: ") et un décalage (prompt
            "shift: "), puis affiche le texte chiffré par César ;
    - "2" : pareil, mais affiche le texte DÉCHIFFRÉ ;
    - "3" : affiche "bye (K operations)" et RENVOIE K, le nombre
            d'opérations 1 ou 2 effectuées ;
    - autre chose : affiche "unknown choice" (ça ne compte pas comme
            une opération).

César : chaque lettre est décalée de `shift` dans l'alphabet (en boucle,
z + 1 -> a), la casse est conservée, les non-lettres ne bougent pas.
Le décalage peut être négatif ou plus grand que 26.

Exemple
    == CIPHER CONSOLE ==
    1) encode  2) decode  3) quit
    choice: 1
    text: Hello, World!
    shift: 3
    Khoor, Zruog!
    choice: 2
    text: Khoor
    shift: 3
    Hello
    choice: 7
    unknown choice
    choice: 3
    bye (2 operations)

Contraintes
    - boucle while ; aucune méthode de str
    - entrées valides : le décalage est toujours un entier

Indice
    Découpe ! Un helper caesar(text, shift) que tu testes SEUL d'abord
    (le déchiffrement, c'est caesar(text, -shift)). Ensuite seulement, la
    boucle principale avec un if / elif / elif / else sur le choix.
    -> Une fois celui-ci fait, le decode_terminal et l'override des TP
       sont des versions plus simples du même programme.

Vérifier : python3 check.py cipher_console
"""


def cipher_console() -> int:
    pass


if __name__ == "__main__":
    print(cipher_console())
