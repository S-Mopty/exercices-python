"""Solution — count_change (niveau 6)."""


def _ways(amount: int, coins: str, i: int) -> int:
    if amount == 0:
        return 1
    if amount < 0 or i == len(coins):
        return 0
    coin = ord(coins[i]) - ord('0')
    # soit on utilise encore la pièce i, soit on ne l'utilise plus jamais
    return _ways(amount - coin, coins, i) + _ways(amount, coins, i + 1)


def count_change(amount: int, coins: str) -> int:
    if amount < 0:
        raise ValueError("Negative amount")
    return _ways(amount, coins, 0)
