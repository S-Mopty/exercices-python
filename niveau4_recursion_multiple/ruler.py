"""
ruler — Niveau 4 ★★   (la structure de Hanoï, en plus simple)

Écris une fonction RÉCURSIVE `ruler(n)` qui dessine les graduations d'une
règle et RENVOIE le nombre de lignes affichées :
    ruler(n) = ruler(n - 1), puis une ligne de n tirets, puis ruler(n - 1)
    ruler(0) n'affiche rien.
Si n < 0 : lever ValueError.

Exemple
    print(ruler(3))
Sortie
    -
    --
    -
    ---
    -
    --
    -
    7

Contraintes
    - récursive ; pour construire UNE ligne de tirets, une boucle est
      autorisée (ou un helper récursif, comme _stars au niveau 3)
    - "-" * n et ** interdits : le nombre de lignes doit venir des valeurs
      renvoyées par les appels récursifs, pas d'une formule

Indice
    La définition ci-dessus EST le code. Le seul travail : récupérer le
    nombre de lignes renvoyé par chacun des deux appels, et renvoyer
    gauche + 1 + droite.
    -> Hanoï a exactement cette forme :
         « faire n-1 », « une action », « refaire n-1 ».

Vérifier : python3 check.py ruler
"""


def ruler(n: int) -> int:
    pass


if __name__ == "__main__":
    print(ruler(3))
