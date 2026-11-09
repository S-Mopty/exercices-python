# Niveau 1 : échauffement, strings et boucles

Objectif : retrouver les réflexes de base sans réfléchir, pour garder toute
ta tête pour les niveaux suivants. Si tout passe en moins d'une heure,
enchaîne directement sur le niveau 2.

| Exercice | ★ | Ce qu'il entraîne |
|---|---|---|
| `count_digits` | ★ | accumulateur, plages de `ord` |
| `remove_char` | ★ | construire une chaîne |
| `swap_case` | ★ | `ord` / `chr`, if / elif / else |
| `find_index` | ★ | parcours par indices, `return` anticipé |
| `is_number` | ★★ | cas particuliers, booléens |
| `count_words` | ★★ | **une variable qui se souvient du tour précédent** |

## Fiche

### Deux façons de parcourir une chaîne

```python
for c in text:              # quand seul le caractère compte
    ...

for i in range(len(text)):  # quand la POSITION compte aussi
    c = text[i]
    ...
```

Prends la première par défaut, et la seconde dès que tu as besoin de `i`
(comparer à la case d'à côté, renvoyer un indice, partir de la fin...).

### Construire une chaîne

Une chaîne ne se modifie pas (`text[0] = "x"` plante). On en construit une
nouvelle, morceau par morceau :

```python
result = ""
for c in text:
    result = result + c     # ajoute à la fin
    # result = c + result   # ajoute au début (ça inverse !)
```

### Lettres et codes

| | codes `ord` |
|---|---|
| `'0'` .. `'9'` | 48 .. 57 |
| `'A'` .. `'Z'` | 65 .. 90 |
| `'a'` .. `'z'` | 97 .. 122 |

Inutile de retenir les nombres : écris `'A' <= c <= 'Z'` ou
`ord('A') <= ord(c) <= ord('Z')`. Pour changer de casse :
`chr(ord(c) - ord('A') + ord('a'))` transforme `'C'` en `'c'`.

### Le `return` dans une boucle

```python
for c in text:
    if c == 'x':
        return True     # trouvé : on peut s'arrêter tout de suite
return False            # on n'arrive ici qu'après avoir TOUT vu
```

Erreur très fréquente : mettre un `else: return False` dans la boucle. La
fonction s'arrête alors dès le premier caractère, sans avoir regardé les
autres.

### Les pièges du niveau

- Le texte vide `""` : teste-le TOUJOURS. Beaucoup de fonctions plantent ou
  renvoient n'importe quoi dessus.
- Renvoyer `1` au lieu de `True` : le correcteur (et la moulinette) font la
  différence.
- `print` au lieu de `return` : la fonction affiche le bon résultat mais
  renvoie `None`.
