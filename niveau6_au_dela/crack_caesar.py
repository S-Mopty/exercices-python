"""
crack_caesar — Niveau 6 ★★★★

On a intercepté un texte anglais chiffré par César, mais on n'a PAS la
clé. Écris `crack_caesar(cipher)` qui retrouve le décalage le plus
probable (entre 0 et 25) qui a servi à le chiffrer.

Méthode imposée (pour que la réponse soit unique) :
    - pour chaque décalage s de 0 à 25, déchiffre `cipher` avec s ;
    - donne une note au texte obtenu : le nombre de lettres parmi
      e, t, a, o, i, n (majuscules comprises) — les 6 lettres les plus
      fréquentes en anglais ;
    - renvoie le s qui a la meilleure note. En cas d'égalité, le plus petit s.

Exemples
    crack_caesar("aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn")   ->  7
    crack_caesar("Nggnpx ng qnja, gura ergerng gb gur fgngvba.")  ->  13
    crack_caesar("")                                              ->  0

    Attention : c'est une méthode STATISTIQUE. Sur un texte très court
    elle peut se tromper : "Wkh vxq lv vklqlqj" (« The sun is shining »,
    décalage 3) donne 23 avec cette note. C'est normal, ce n'est pas un
    bug de ton code. Plus le texte est long, plus elle est fiable.

Contraintes
    - boucles obligatoires
    - pas de listes pour stocker les 26 essais : garde seulement le
      meilleur au fur et à mesure

Indice
    Trois fonctions : decode(text, shift), score(text), et crack_caesar
    qui boucle sur les 26 décalages avec le pattern « meilleur jusqu'ici »
    (comme longest_run). Utiliser > et pas >= gère tout seul les égalités.
    Bonus (non testé) : déchiffre ce message avec ta fonction :
        "Kyv crjk xyfjk ze kyv Tfiv wzerccp ivjkj."

Vérifier : python3 check.py crack_caesar
"""


def crack_caesar(cipher: str) -> int:
    pass


if __name__ == "__main__":
    print(crack_caesar("aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn"))
