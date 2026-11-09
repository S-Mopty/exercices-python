"""Solution — hanoi (niveau 4)."""


def hanoi(n: int, src: str, aux: str, dst: str) -> int:
    if n < 0:
        raise ValueError("Invalid disk count")
    if n == 0:
        return 0
    # 1. les n-1 du dessus : de src vers aux (dst sert d'intermédiaire)
    before = hanoi(n - 1, src, dst, aux)
    # 2. le disque n, enfin libre : de src vers dst
    print("disk " + str(n) + ": " + src + " -> " + dst)
    # 3. les n-1 : de aux vers dst (src sert d'intermédiaire)
    after = hanoi(n - 1, aux, src, dst)
    return before + 1 + after


# La version du TP (fonction à un seul paramètre, tours A/B/C fixes) n'est
# qu'un « emballage » : unlock_gate(n) vérifie n puis appelle un helper
# _move(n, "A", "B", "C") qui a exactement la structure ci-dessus.
