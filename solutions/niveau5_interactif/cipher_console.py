"""Solution — cipher_console (niveau 5)."""


def caesar(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            c = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        result = result + c
    return result


def cipher_console() -> int:
    print("== CIPHER CONSOLE ==")
    print("1) encode  2) decode  3) quit")
    operations = 0
    choice = input("choice: ")
    while choice != "3":
        if choice == "1" or choice == "2":
            text = input("text: ")
            shift = int(input("shift: "))
            if choice == "2":
                shift = -shift          # déchiffrer = chiffrer à l'envers
            print(caesar(text, shift))
            operations = operations + 1
        else:
            print("unknown choice")
        choice = input("choice: ")
    print("bye (" + str(operations) + " operations)")
    return operations
