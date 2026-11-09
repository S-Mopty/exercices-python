"""Solution — sum_until_zero (niveau 5)."""


def sum_until_zero() -> int:
    total = 0
    count = 0
    value = int(input("number: "))      # lecture AVANT la boucle...
    while value != 0:
        total = total + value
        count = count + 1
        value = int(input("number: "))  # ... et à la FIN de chaque tour
    print("total: " + str(total) + " (" + str(count) + " numbers)")
    return total
