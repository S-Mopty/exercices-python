# Niveau 4 : récursion à plusieurs appels, la route vers Hanoï

Au niveau 3, chaque appel en faisait **un seul** autre : une chaîne
d'appels. Ici, chaque appel en fait **deux ou plus** : un **arbre**
d'appels. C'est la forme de Hanoï, et c'est là que « dérouler dans sa tête »
devient impossible. Il faut changer de méthode.

| Exercice | ★ | Ce qu'il entraîne |
|---|---|---|
| `predict` | ★★ | **lire un arbre d'appels** sans exécuter |
| `ruler` | ★★ | « faire n-1, une action, refaire n-1 » : **le squelette de Hanoï** |
| `binary_words` | ★★★ | paramètre accumulateur (`prefix`), deux branches |
| `grid_paths` | ★★★ | additionner les résultats de deux appels |
| `fibo` | ★★★ | compter les appels par les `return` |
| `hanoi` | ★★★★ | **le boss** : paramètres qui changent de rôle |
| `permutations` | ★★★★ | une boucle de choix + récursion |

Fais `predict` en premier, sur papier.

## Fiche

### L'arbre d'appels

```python
def f(n):
    if n == 0:
        return
    print(n)
    f(n - 1)
    f(n - 1)
```

Chaque appel `f(n)` avec `n > 0` fait deux appels `f(n - 1)` :

```
                      f(3) : print 3
                 ┌────────┴────────┐
         f(2) : print 2      f(2) : print 2
          ┌─────┴─────┐       ┌─────┴─────┐
        f(1)        f(1)    f(1)        f(1)       <- chacun : print 1
        /  \        /  \    /  \        /  \
      f(0) f(0)  f(0) f(0) f(0) f(0)  f(0) f(0)    <- cas de base
```

**L'ordre d'exécution**, c'est un parcours en profondeur, de gauche à
droite : on descend tout à gauche, on remonte, on descend dans la branche
suivante... Un appel ne passe à sa deuxième branche qu'après avoir
**entièrement** fini la première.

Ici le `print` est **avant** les deux appels, donc chaque nœud affiche en
arrivant : `3 2 1 1 2 1 1`. Et il y a 15 appels en tout (compte les nœuds).

Et si le `print` était **entre** les deux appels ? Ou **après** ? C'est la
question 1 de `predict.py`.

### Pour écrire : ne déroule pas, fais confiance

Pour **lire** un arbre, on le dessine. Pour **écrire** une fonction qui en
produit un, on ne pense qu'à **un seul nœud** :

> « Si les appels sur `n - 1` font correctement leur travail, qu'est-ce que
> MOI je dois faire autour ? »

Pour `ruler` : si `ruler(n - 1)` dessine correctement une petite règle, alors
une règle de taille `n` = petite règle, ma graduation de `n` tirets, petite
règle. C'est tout. On ne se demande jamais comment `ruler(n - 1)` s'y prend.

### Compter avec les `return`

```
compte(n) = compte(branche gauche) + ma part + compte(branche droite)
```

Chaque appel renvoie combien de lignes (ou de déplacements, ou d'appels) il
a produits, **lui et tout son sous-arbre**. Le parent additionne. Pas de
variable globale, pas de formule toute faite.

### Hanoï : pourquoi ça marche

Prenons 3 disques, à amener de `src` vers `dst`. Le contenu de chaque tour
est écrit de bas en haut :

```
                  src      aux      dst
Départ        :   3 2 1    .        .
Après étape 1 :   3        2 1      .         (les 2 petits sont sur aux)
Après étape 2 :   .        2 1      3         (le grand est passé)
Après étape 3 :   .        .        3 2 1     (les 2 petits l'ont rejoint)
```

- **Étape 2** : un seul déplacement, le disque 3. Il n'est possible que si
  les disques 1 et 2 sont ailleurs que sur `src` et sur `dst`, donc sur `aux`.
- **Étape 1** : c'est le problème « déplacer 2 disques », mais de `src`
  vers `aux`. Pendant ce temps, c'est `dst` qui sert de tour intermédiaire.
- **Étape 3** : encore « déplacer 2 disques », cette fois de `aux` vers
  `dst`, avec `src` comme intermédiaire.

Les étapes 1 et 3 sont **le même problème en plus petit**, mais avec des
tours qui jouent **d'autres rôles**. C'est pour ça que la fonction prend les
noms des tours en paramètres : à chaque appel récursif, on les passe dans
un ordre différent. Toute la difficulté de l'exercice est de trouver ces
deux ordres. Avec le tableau ci-dessus, c'est faisable.

Et le nombre de déplacements suit le même schéma que `ruler` :
`dép(n) = dép(n - 1) + 1 + dép(n - 1)`.

### Le paramètre accumulateur

Pour **générer** des objets (mots binaires, permutations), on passe en
paramètre ce qu'on a déjà construit :

```
_gen(prefix, remaining)
    remaining == 0  -> prefix est un objet complet : on l'affiche
    sinon           -> une branche par choix possible : _gen(prefix + choix, ...)
```

`prefix` est le chemin parcouru depuis la racine de l'arbre.

### Les pièges du niveau

- **Ne pas récupérer les deux `return`** : `ruler(n - 1)` appelé deux fois,
  mais une seule valeur additionnée.
- **Échanger les rôles des tours au mauvais endroit** : si tes déplacements
  ont le bon nombre de lignes mais les mauvaises tours, reprends le tableau
  « src / aux / dst » ci-dessus, étape par étape.
- **Vouloir tout dérouler** : au-delà de n = 2, c'est impossible de tête.
  Vérifie n = 0, n = 1, n = 2 à la main, et fais confiance pour le reste.
