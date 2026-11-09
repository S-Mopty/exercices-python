# Niveau 5 : programmes interactifs (`while` + `input`)

Les bonus `decode_terminal` et `override` ne sont pas durs
algorithmiquement. Ce qui coince, c'est la **structure** : quand lire,
quand s'arrêter, quoi afficher exactement. Ce niveau entraîne ça.

| Exercice | ★ | Ce qu'il entraîne |
|---|---|---|
| `echo_upper` | ★★ | **boucle sentinelle**, compter les tours |
| `sum_until_zero` | ★★ | `int(input())`, sentinelle numérique |
| `guess` | ★★ | sortir de la boucle avec `return` |
| `min_max` | ★★★ | traiter des valeurs « au vol », sans les stocker |
| `cipher_console` | ★★★★ | **le boss** : menu, helpers, tout le bloc 1 |

## Fiche

### `input()` renvoie toujours une chaîne

```python
x = input("number: ")       # x vaut "5", pas 5
n = int(input("number: "))  # n vaut 5
```

`"5" + "3"` vaut `"53"`, et `5 + "3"` plante (`TypeError`). Convertis dès
la lecture si tu as besoin d'un nombre.

### Les deux squelettes de boucle sentinelle

Une boucle sentinelle lit des valeurs jusqu'à une valeur spéciale (`STOP`,
`0`, `QUIT`...). Les deux squelettes à connaître :

```python
# A. while True + sortie explicite
while True:
    line = input("> ")
    if line == "STOP":
        ...                 # ce qu'on fait à la fin
        return ...          # (ou break)
    ...                     # traitement normal

# B. lecture avant la boucle, puis à la fin de chaque tour
line = input("> ")
while line != "STOP":
    ...                     # traitement normal
    line = input("> ")      # relire, en DERNIER
...                         # ce qu'on fait à la fin
```

Le B force à écrire `input` deux fois. Le A est souvent plus simple à
lire. Erreur classique avec le B : relire au **début** du tour, donc avant
d'avoir traité la ligne précédente, qui est perdue.

### Prompts et affichages : au caractère près

La moulinette compare ta sortie avec la sortie attendue **caractère par
caractère**. `"number:"` au lieu de `"number: "` (l'espace !), `"Stop"` au
lieu de `"STOP"`, une ligne vide en trop : c'est faux.

`input("> ")` et `print("> ", end="")` suivi de `input()` donnent exactement
le même affichage. Si le sujet impose l'un des deux, respecte-le.

### Comment le correcteur simule le clavier

Le correcteur « tape » les entrées à ta place et les affiche après le
prompt, comme dans un vrai terminal. La sortie attendue dans les consignes
contient donc ce que l'utilisateur tape :

```
> hello          <- "> " est affiché par ton programme, "hello" est tapé
HELLO            <- affiché par ton programme
```

Si ton programme demande une entrée de trop, il le détecte et te le dit,
au lieu de rester bloqué.

### Découper avant d'assembler

Pour un programme comme `cipher_console` :

1. écris le helper `caesar(text, shift)` et teste-le **seul** ;
2. écris la boucle principale avec juste le choix `"3"` (quitter) ;
3. ajoute les choix un par un, en testant à chaque fois.

Écrire tout d'un coup puis déboguer le tout, c'est la recette pour passer
une heure sur une faute de frappe.

### Les pièges du niveau

- Comparer une entrée non convertie à un nombre : `input() == 0` est
  toujours faux (c'est `"0" == 0`).
- Compter la sentinelle comme une vraie valeur (`STOP` compté comme une
  ligne, le `0` final compté comme un nombre).
- Oublier le `return` final : la fonction affiche tout bien mais renvoie
  `None`.
