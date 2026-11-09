"""Solution — n_queens (niveau 6)."""


def _abs(x: int) -> int:
    if x < 0:
        return -x
    return x


def _safe(placed: str, c: int) -> bool:
    """La colonne c de la ligne len(placed) est-elle attaquée ?"""
    row = len(placed)
    for r in range(row):
        qc = ord(placed[r]) - ord('0')
        if qc == c or _abs(qc - c) == row - r:
            return False
    return True


def _solve(n: int, placed: str) -> int:
    if len(placed) == n:
        return 1                                  # toutes les reines sont posées
    total = 0
    for c in range(n):
        if _safe(placed, c):
            total = total + _solve(n, placed + chr(c + ord('0')))
    return total


def n_queens(n: int) -> int:
    if n < 0 or n > 9:
        raise ValueError("Unsupported size")
    return _solve(n, "")
