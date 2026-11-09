"""Solution — min_max (niveau 5)."""


def min_max() -> None:
    n = int(input("how many? "))
    if n <= 0:
        print("nothing to do")
        return
    first = int(input("> "))
    smallest = first            # initialisés avec le premier nombre, pas avec 0
    largest = first
    for _ in range(n - 1):
        value = int(input("> "))
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    print("min: " + str(smallest))
    print("max: " + str(largest))
