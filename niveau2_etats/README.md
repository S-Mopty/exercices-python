# Niveau 2 : boucles à plusieurs variables d'état

C'est **le** niveau qui débloque `vigenere_decode`. Dans les exercices
obligatoires, chaque tour de boucle est indépendant des autres. Ici, pour
décider quoi faire à un tour, il faut se souvenir de ce qui s'est passé
avant, et parfois faire avancer un compteur à un autre rythme que la boucle.

| Exercice | ★ | Ce qu'il entraîne |
|---|---|---|
| `alternate_case` | ★★ | **un compteur qui n'avance pas à chaque tour** |
| `repeat_to_length` | ★★ | **le modulo pour faire boucler un indice** |
| `interleave` | ★★ | deux chaînes de longueurs différentes |
| `compress` | ★★ | caractère précédent + compteur, le piège du dernier bloc |
| `longest_run` | ★★ | « meilleur jusqu'ici » |
| `parse_int` | ★★★ | résultat partiel (Horner), validation |
| `digit_cipher` | ★★★ | tout ensemble : **c'est un Vigenère déguisé** |
| `find_sub` | ★★★ | boucles imbriquées avec indices |

## Fiche

### La question à se poser

> « Qu'est-ce que je dois savoir sur le PASSÉ pour décider quoi faire
> MAINTENANT ? »

Chaque réponse à cette question, c'est une variable à créer **avant** la
boucle et à mettre à jour **dans** la boucle.

### Exemple travaillé : compter les montées

On veut compter combien de fois un chiffre est plus grand que celui qui le
précède : dans `"13254"`, il y a 2 montées (1→3 et 2→5).

Pour savoir si c'est une montée, il faut connaître le chiffre précédent.
Une variable d'état `previous` :

```python
def count_rises(digits):
    rises = 0
    previous = ""                    # rien vu pour l'instant
    for c in digits:
        if previous != "" and c > previous:
            rises = rises + 1
        previous = c                 # mise à jour EN DERNIER
    return rises
```

Le tableau de trace, à faire sur papier tant que ça ne marche pas :

| tour | `c` | `previous` au début du tour | montée ? | `rises` | `previous` à la fin |
|---|---|---|---|---|---|
| 1 | `'1'` | `""` | non (rien avant) | 0 | `'1'` |
| 2 | `'3'` | `'1'` | oui | 1 | `'3'` |
| 3 | `'2'` | `'3'` | non | 1 | `'2'` |
| 4 | `'5'` | `'2'` | oui | 2 | `'5'` |
| 5 | `'4'` | `'5'` | non | 2 | `'4'` |

Note l'ordre : on **utilise** `previous`, puis on le **met à jour**. Dans
l'autre sens, on comparerait `c` à lui-même.

### Deux vitesses : la boucle et le compteur

La boucle avance d'un caractère à chaque tour. Mais un compteur peut avancer
à **son propre rythme**, seulement quand une condition est vraie :

```python
k = 0                          # avance à SON rythme
for c in text:                 # avance à chaque caractère
    if <c est une lettre>:
        ... utiliser k ...
        k = k + 1              # seulement ici
    else:
        ...                    # k ne bouge pas
```

C'est exactement ce que demande un Vigenère : la boucle passe sur tous les
caractères du message, mais l'index dans la clé n'avance que sur les
lettres.

### Faire boucler un indice : le modulo

Pour parcourir une clé courte en boucle, `key[k % len(key)]` donne
`key[0], key[1], key[2], key[0], key[1]...`. Retiens cette formule, elle
revient tout le temps.

Et pour l'alphabet : `(position + décalage) % 26` gère tout, même un
décalage négatif. En Python, `(-3) % 26` vaut `23`.

### Les pièges du niveau

- **Le dernier bloc** (`compress`, `count_words`...) : si tu « écris » un
  bloc quand le caractère change, le dernier bloc n'est jamais écrit, car
  rien ne change après lui. Traite-le après la boucle.
- **L'initialisation** : `best = 0` marche pour une longueur, mais pas pour
  un minimum (voir `min_max` au niveau 5). Demande-toi toujours si la
  valeur de départ peut fausser le premier tour.
- **Mettre à jour dans le mauvais ordre** : voir l'exemple ci-dessus.
