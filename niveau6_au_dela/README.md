# Niveau 6 : au-delà des TP

Mêmes règles qu'avant (toujours pas de listes), mais des problèmes plus
gros, où la difficulté n'est plus la syntaxe mais **l'organisation** :
découper en helpers, choisir comment représenter l'état, tester les
morceaux séparément. C'est ce qui fait la différence en exam.

| Exercice | ★ | Ce qu'il entraîne |
|---|---|---|
| `roman` | ★★★ | factoriser un schéma répétitif dans un helper |
| `add_big` | ★★★ | deux indices depuis la fin, retenue |
| `look_and_say` | ★★★ | réutiliser un exercice précédent (`compress`) |
| `crack_caesar` | ★★★★ | boucle sur des essais, « meilleur jusqu'ici », méthode statistique |
| `balanced` | ★★★★ | **une pile sans liste** (une chaîne) |
| `count_change` | ★★★★ | récursion à deux branches : « je prends / je ne prends plus » |
| `n_queens` | ★★★★★ | **backtracking** : le boss final |

## Fiche

### Attaquer un problème plus gros

1. **Exemples à la main.** Fais au moins deux exemples complets sur papier,
   dont un cas limite (vide, 0, 1).
2. **Liste les sous-problèmes.** Pour `roman` : « écrire UN chiffre décimal
   avec trois symboles » est un sous-problème. Il devient un helper.
3. **Teste chaque helper seul**, sous `if __name__ == "__main__":`, avant
   de les assembler.
4. **Nomme bien.** `_digit(d, one, five, ten)` se relit ; `f(a, b, c, d)`
   non.

### Représenter un état sans liste

Pas de liste ? Une chaîne fait très bien l'affaire pour beaucoup de choses :

| Besoin | Avec une chaîne |
|---|---|
| une pile (`balanced`) | empiler : `s = s + c` · sommet : `s[len(s) - 1]` · dépiler : reconstruire sans le dernier caractère |
| des positions (`n_queens`) | une chaîne de chiffres : `placed[r]` = colonne de la reine de la ligne `r` |
| un ensemble de choix (`count_change`) | une chaîne + un indice qui avance |

Quand tu verras les listes en cours, tu retrouveras exactement les mêmes
idées, en plus pratique.

### Le backtracking

`n_queens` (et `permutations`, au niveau 4) suivent ce schéma :

```
explorer(état) :
    si l'état est complet :
        c'est une solution -> compter 1
    sinon, pour chaque choix possible :
        si le choix est compatible avec l'état :
            explorer(état + choix)
```

On essaie, on descend, et quand une branche est finie (ou impossible) on
revient automatiquement au choix suivant : c'est le retour de l'appel
récursif qui fait le « retour en arrière ». Le test de compatibilité
**coupe** les branches inutiles, et c'est ce qui rend la recherche rapide.

### Un mot sur la vitesse

`grid_paths(15, 15)` au niveau 4 est très lent : le même sous-problème est
recalculé des millions de fois (compte les appels, comme pour `fibo_calls`).
La solution (retenir les résultats déjà calculés, la *mémoïsation*)
demande un dictionnaire : ce sera pour quand vous les aurez vus en cours.
