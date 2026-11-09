"""Solution — fibo / fibo_calls (niveau 4)."""


def fibo(n: int) -> int:
    if n < 0:
        raise ValueError("Invalid index")
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def fibo_calls(n: int) -> int:
    if n < 0:
        raise ValueError("Invalid index")
    if n <= 1:
        return 1                    # fibo(0) et fibo(1) ne rappellent rien
    return 1 + fibo_calls(n - 1) + fibo_calls(n - 2)
