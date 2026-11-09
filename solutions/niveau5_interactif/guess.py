"""Solution — guess (niveau 5)."""


def guess(secret: int) -> int:
    tries = 0
    while True:
        value = int(input("guess: "))
        tries = tries + 1
        if value < secret:
            print("too low")
        elif value > secret:
            print("too high")
        else:
            if tries == 1:
                print("found in 1 try!")
            else:
                print("found in " + str(tries) + " tries!")
            return tries
