"""
balanced — Niveau 6 ★★★★

La version « pro » du is_stable du TP : écris `balanced(code)` qui renvoie
True si les parenthèses (), crochets [] et accolades {} de `code` sont
correctement appariées et imbriquées, False sinon. Les autres caractères
sont ignorés.

Exemples
    balanced("([]{})")        ->  True
    balanced("a(b[c]d)e")     ->  True
    balanced("{[()()]}")      ->  True
    balanced("([)]")          ->  False   (bien comptés, mal imbriqués)
    balanced("((")            ->  False
    balanced("}")             ->  False
    balanced("")              ->  True

Contraintes
    - boucle obligatoire, pas de listes

Indice
    Un simple compteur ne suffit plus : "([)]" a autant d'ouvrants que de
    fermants. Il faut une PILE : on empile chaque ouvrant ; sur un
    fermant, le sommet de la pile doit être l'ouvrant correspondant, et on
    le dépile.
    Pas de liste ? Une chaîne fait une très bonne pile :
        empiler  : stack = stack + c
        sommet   : stack[len(stack) - 1]
        dépiler  : reconstruire stack sans son dernier caractère
                   (helper avec une boucle, le slicing est interdit)

Vérifier : python3 check.py balanced
"""


def balanced(code: str) -> bool:
    pass


if __name__ == "__main__":
    print(balanced("{[()()]}"))
