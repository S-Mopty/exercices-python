# Niveau 3 : la récursion, l'ordre d'exécution et les helpers

Tu sais déjà écrire une récursion simple (compte à rebours, somme des
chiffres). Ce niveau installe les trois idées dont Hanoï a besoin :

1. ce qui est écrit **après** l'appel récursif s'exécute **au retour** ;
2. un résultat se construit en **récupérant** la valeur renvoyée par
   l'appel récursif ;
3. quand il faut plus d'informations que les paramètres imposés, on écrit
   un **helper avec des paramètres en plus**.

| Exercice | ★ | Ce qu'il entraîne |
|---|---|---|
| `power` | ★ | les 3 questions |
| `count_up` | ★ | **print après l'appel** |
| `bounce` | ★★ | print avant ET après, **compte qui remonte** |
| `count_digit` | ★★ | récursion sur les chiffres, bien choisir le cas de base |
| `reverse_rec` | ★★ | **helper avec un indice** |
| `is_palindrome_rec` | ★★★ | helper avec deux indices |
| `stars_triangle` | ★★★ | deux fonctions récursives qui coopèrent |
| `from_base` | ★★★ | helper + validation + calcul |

## Fiche

### Les 3 questions

Pour écrire **n'importe quelle** fonction récursive :

1. **Cas de base** : pour quelle entrée je connais la réponse sans calcul ?
2. **Cas récursif** : *si on me donne* la réponse pour une entrée plus
   petite, comment je fabrique la réponse pour la mienne ?
3. **Terminaison** : est-ce que chaque appel se rapproche du cas de base ?

Le « si on me donne » est le cœur de la méthode : quand tu écris le cas
récursif, **tu ne te demandes pas comment l'appel récursif fait son
travail**. Tu supposes qu'il le fait. C'est le *leap of faith*.

### Avant ou après l'appel : la pile d'appels

```python
def countdown(n):
    if n == 0:
        return
    print(n)            # AVANT l'appel
    countdown(n - 1)
```

`countdown(3)` affiche `3 2 1`. Voici ce qui se passe, chaque appel étant
« en pause » tant que celui du dessous n'a pas fini :

```
countdown(3)
│  print(3)
│  countdown(2)
│  │  print(2)
│  │  countdown(1)
│  │  │  print(1)
│  │  │  countdown(0)  -> cas de base, return
│  │  └─ fini
│  └─ fini
└─ fini
```

Si on échange les deux lignes (appel PUIS print), chaque `print` attend que
tout ce qui est en dessous soit fini. Ils s'exécutent donc en remontant :
`1`, puis `2`, puis `3`. C'est l'exercice `count_up`.

### Faire remonter une valeur

```python
def total(n):                   # 1 + 2 + ... + n
    if n == 0:
        return 0
    rest = total(n - 1)         # je fais confiance : rest = 1 + ... + (n-1)
    return rest + n             # j'ajoute MA part
```

```
total(3) = total(2) + 3
         = (total(1) + 2) + 3
         = ((total(0) + 1) + 2) + 3
         = ((0 + 1) + 2) + 3
         = 6
```

Le schéma « je récupère le résultat du sous-problème, j'ajoute ma part, je
renvoie », c'est comme ça que Hanoï compte ses déplacements. Et ça
explique pourquoi `global` est interdit : on n'en a pas besoin, l'information
remonte par les `return`.

### Le helper avec des paramètres en plus

Sans slicing, on ne peut pas raccourcir une chaîne à chaque appel. On ajoute
donc un **indice** qui dit où on en est, dans une fonction auxiliaire :

```python
def count_char(text, c):                 # le prototype imposé
    return _count_from(text, c, 0)       # il ne fait que lancer le helper

def _count_from(text, c, i):
    """Nombre de c dans text à partir de l'indice i."""
    if i == len(text):                   # plus rien à regarder
        return 0
    here = 0
    if text[i] == c:
        here = 1
    return here + _count_from(text, c, i + 1)
```

Ce découpage « fonction imposée → helper qui a ce qu'il faut comme
paramètres » est exactement celui du bonus Hanoï du TP (`unlock_gate(n)`
appelle un `_move(n, src, aux, dst)`).

### Les pièges du niveau

```python
def total(n):
    if n == 0:
        return 0
    total(n - 1) + n        # calculé... puis jeté : il manque le return !
```

- **Oublier le `return`** devant le calcul récursif : la fonction renvoie
  `None`.
- **Cas de base jamais atteint** (`n == 0` alors que `n` peut être
  négatif, ou un indice qui saute par-dessus `len(text)`) :
  `RecursionError`.
- **Mélanger `print` et `return`** : une fonction qui doit renvoyer une
  chaîne ne doit rien afficher.
