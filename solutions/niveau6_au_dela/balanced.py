"""Solution — balanced (niveau 6)."""


def _pop(stack: str) -> str:
    """stack sans son dernier caractère."""
    result = ""
    for i in range(len(stack) - 1):
        result = result + stack[i]
    return result


def _opening(closing: str) -> str:
    if closing == ')':
        return '('
    if closing == ']':
        return '['
    return '{'


def balanced(code: str) -> bool:
    stack = ""
    for c in code:
        if c == '(' or c == '[' or c == '{':
            stack = stack + c                       # empiler
        elif c == ')' or c == ']' or c == '}':
            if len(stack) == 0:
                return False                        # fermant sans ouvrant
            if stack[len(stack) - 1] != _opening(c):
                return False                        # mauvais ouvrant au sommet
            stack = _pop(stack)                     # dépiler
    return len(stack) == 0                          # tout a été refermé ?
