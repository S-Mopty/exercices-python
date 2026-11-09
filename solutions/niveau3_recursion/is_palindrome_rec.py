"""Solution — is_palindrome_rec (niveau 3)."""


def _check(text: str, left: int, right: int) -> bool:
    if left >= right:
        return True
    if text[left] == ' ':
        return _check(text, left + 1, right)
    if text[right] == ' ':
        return _check(text, left, right - 1)
    if text[left] != text[right]:
        return False
    return _check(text, left + 1, right - 1)


def is_palindrome_rec(text: str) -> bool:
    return _check(text, 0, len(text) - 1)
