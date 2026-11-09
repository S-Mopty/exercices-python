"""
echo_upper — Niveau 5 ★★

Écris `echo_upper()` qui, en boucle :
    - lit une ligne avec le prompt "> " ;
    - si la ligne est exactement "STOP" : affiche "K line(s) echoed."
      (K = nombre de lignes répétées) et RENVOIE K ;
    - sinon : affiche la ligne en MAJUSCULES et recommence.

Exemple (ce que tu verrais dans le terminal ; après "> ", c'est toi qui tapes)
    > hello
    HELLO
    > Python 3
    PYTHON 3
    > STOP
    2 line(s) echoed.

Contraintes
    - boucle while obligatoire ; pas de .upper() (écris un helper to_upper)
    - "STOP" est sensible à la casse : "stop" est répété comme le reste
    - input("> ") ou print("> ", end="") puis input() : les deux marchent

Indice
    Deux squelettes classiques, à connaître tous les deux :

        while True:                      line = input("> ")
            line = input("> ")           while line != "STOP":
            if line == "STOP":               ...
                ...                          line = input("> ")
                return ...               ...
            ...

    Celui de droite lit une première fois AVANT la boucle, puis à la FIN
    de chaque tour. Les deux sont acceptés.

Vérifier : python3 check.py echo_upper
"""


def echo_upper() -> int:
    pass


if __name__ == "__main__":
    print(echo_upper())
