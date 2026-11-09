# Exercices Python : de « je bloque aux bonus » à « à l'aise »

41 exercices progressifs, avec un correcteur automatique façon moulinette,
pour quelqu'un qui réussit la partie obligatoire des TP de prog (boucles,
strings, récursion simple) mais qui cale sur les bonus.

## Le diagnostic

Les bonus des TP ne sont pas « la même chose en plus dur ». Ils demandent
trois compétences que les exercices obligatoires entraînent à peine :

| Compétence | Exemple de bonus | Où on l'entraîne |
|---|---|---|
| Faire évoluer **plusieurs variables d'état** dans une boucle (dont une qui n'avance pas à chaque tour) | `vigenere_decode` : la clé n'avance que sur les lettres | Niveau 2 |
| Penser une **récursion à plusieurs appels**, avec des **paramètres en plus**, et faire remonter un compte par les `return` | `unlock_gate` (Hanoï) | Niveaux 3 et 4 |
| Structurer un **programme interactif** : `while` + `input`, condition d'arrêt, prompts exacts | `decode_terminal`, `override` | Niveau 5 |

Le niveau 6 va au-delà des TP : problèmes plus gros, mêmes contraintes.

## Démarrer

Il faut Python 3.8 ou plus récent. Sous Windows, remplace `python3` par
`python` (ou `py`).

```bash
git clone https://github.com/S-Mopty/exercices-python.git
```

```bash
cd exercices-python
```

```bash
python3 check.py
```

Ensuite, pour chaque exercice :

1. Ouvre le fichier (ex : `niveau2_etats/compress.py`). La consigne est en
   haut, dans le docstring.
2. Remplace le `pass` par ton code. Tes tests perso vont sous
   `if __name__ == "__main__":`.
3. Lance le correcteur sur cet exercice :

```bash
python3 check.py compress
```

Autres façons de lancer le correcteur :

| Commande | Effet |
|---|---|
| `python3 check.py` | tous les exercices |
| `python3 check.py 3` | tout le niveau 3 |
| `python3 check.py compress ruler` | plusieurs exercices |
| `python3 check.py --express` | seulement le parcours express |

Le correcteur te dit quelle règle n'est pas respectée et, pour le premier
test raté, la première ligne qui diffère. Un exercice encore à `pass` est
marqué **À FAIRE**, ce n'est pas une erreur.

## Les règles (celles de la moulinette des TP)

**Autorisé :** `print`, `len`, `int`, `str`, `input`, `ord`, `chr`,
`range`, `ValueError`, les `if` / `for` / `while`, `def` / `return` /
`raise`, les opérateurs, l'indexation `s[i]` (sauf mention contraire),
les f-strings.

**Interdit partout :** les méthodes (`.lower()`, `.split()`, `.count()`...),
le slicing `s[a:b]`, les listes / tuples / dictionnaires / sets, `import`,
`global`, `lambda`, et les autres builtins (`max`, `min`, `sum`, `abs`,
`sorted`...).

**Certains exercices ajoutent** une contrainte : récursion obligatoire,
aucune boucle, pas de `**`, pas de `int()`... C'est écrit dans la consigne,
et le correcteur le vérifie.

Ces interdictions ne sont pas là pour embêter. Se priver des raccourcis
oblige à penser l'algorithme, et c'est exactement ce que l'exam évalue.

## Le parcours

Chaque niveau a une **fiche de cours** (`README.md` dans son dossier) : lis-la
avant d'attaquer les exercices.

| Niveau | Dossier | Thème | Exos |
|---|---|---|---|
| 1 | `niveau1_strings` | Échauffement : strings et boucles | 6 |
| 2 | `niveau2_etats` | Boucles à plusieurs variables d'état | 8 |
| 3 | `niveau3_recursion` | Récursion : l'ordre d'exécution, les helpers | 8 |
| 4 | `niveau4_recursion_multiple` | Récursion à plusieurs appels, jusqu'à Hanoï | 7 |
| 5 | `niveau5_interactif` | Programmes interactifs (`while` + `input`) | 5 |
| 6 | `niveau6_au_dela` | Au-delà des TP | 7 |

Difficulté : ★ (5 min) à ★★★★★ (une bonne heure).

### Parcours express (14 exercices)

Si le temps presse, ces 14 exercices visent droit sur les bonus, sans le
reste :

```bash
python3 check.py --express
```

`count_words` → `alternate_case` → `compress` → `digit_cipher` →
`count_up` → `bounce` → `reverse_rec` → `stars_triangle` → `predict` →
`ruler` → `binary_words` → `hanoi` → `echo_upper` → `cipher_console`

## La méthode (le plus important)

1. **Fais l'exemple à la main avant de coder.** Si tu ne sais pas le faire
   sur papier, tu ne sais pas le coder, et taper au hasard n'y changera rien.
2. **Trace tes variables.** Un tableau avec une ligne par tour de boucle et
   une colonne par variable. C'est lent, et c'est ce qui débloque.
3. **Récursion : ne déroule pas tout dans ta tête.** Pose-toi les 3
   questions de la fiche du niveau 3 et fais confiance à l'appel récursif.
4. **Bloqué plus de 10 min :** lis l'indice en bas de la consigne.
5. **Bloqué plus de 20 min de plus :** regarde la solution dans
   `solutions/`, **ferme-la**, et réécris l'exercice de mémoire le
   lendemain. Une solution lue sans être refaite ne compte pas.

## Le vrai test : retour aux TP

Quand les niveaux 2, 4 et 5 sont verts, refais les bonus des TP **à partir
d'un fichier vide**, sans regarder ton ancien code. Objectif : moins de
20 minutes chacun.

| Bonus du TP | Exercice qui y prépare |
|---|---|
| `vigenere_decode` | `digit_cipher` (même mécanique, avec des chiffres au lieu de lettres) |
| `decode_terminal` | `echo_upper`, `cipher_console` |
| `unlock_gate` | `hanoi` (même algorithme : tours A/B/C fixées, autre format de ligne) |
| `override` | `cipher_console` |

## Structure du dépôt

```
exercices-python/
├── check.py                      # le correcteur
├── niveau1_strings/ ... niveau6_au_dela/
│   ├── README.md                 # la fiche de cours du niveau
│   └── *.py                      # les exercices (consigne + squelette)
├── solutions/                    # les corrigés commentés (après avoir essayé !)
└── tests/                        # les tests utilisés par check.py
```

Les solutions passent toutes le correcteur :

```bash
python3 check.py --solutions
```
