"""Solution — echo_upper (niveau 5)."""


def to_upper(text: str) -> str:
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - ord('a') + ord('A'))
        result = result + c
    return result


def echo_upper() -> int:
    count = 0
    while True:
        line = input("> ")
        if line == "STOP":
            print(str(count) + " line(s) echoed.")
            return count
        print(to_upper(line))
        count = count + 1
