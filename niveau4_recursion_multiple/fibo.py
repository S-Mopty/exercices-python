"""
fibo — Niveau 4 ★★★  (deux fonctions dans ce fichier)

1) `fibo(n)` renvoie le n-ième nombre de Fibonacci, de façon RÉCURSIVE
   « naïve » : fibo(0) = 0, fibo(1) = 1, fibo(n) = fibo(n-1) + fibo(n-2).

2) `fibo_calls(n)` renvoie le NOMBRE D'APPELS à fibo que déclenche le
   calcul de fibo(n), en comptant l'appel fibo(n) lui-même.
   fibo_calls ne doit PAS appeler fibo : elle compte, elle ne calcule pas.

Si n < 0 : lever ValueError (dans les deux fonctions).

Exemples
    fibo(10)        ->  55
    fibo_calls(0)   ->  1
    fibo_calls(2)   ->  3      (fibo(2) appelle fibo(1) et fibo(0))
    fibo_calls(10)  ->  177

Contraintes
    - récursives, aucune boucle
    - pas de variable globale pour compter (global est interdit) : le
      compte doit remonter par les return

Indice
    Dessine l'arbre des appels de fibo(4) sur papier et compte les nœuds.
    Un appel à fibo(n) = 1 (lui-même) + les appels faits par fibo(n - 1)
    + les appels faits par fibo(n - 2). Pense aux cas n = 0 et n = 1.
    -> Hanoï : nb de déplacements(n) = déplacements(n-1) + 1 + déplacements(n-1).
       C'est le même raisonnement.

Vérifier : python3 check.py fibo
"""


def fibo(n: int) -> int:
    pass


def fibo_calls(n: int) -> int:
    pass


if __name__ == "__main__":
    print(fibo(10), fibo_calls(10))
