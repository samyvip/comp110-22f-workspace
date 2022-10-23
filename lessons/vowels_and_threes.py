"""Quiz 03 Practice."""


def vowels_and_threes(a: str) -> str:
    """Returns characters at index that is multiple of 3 or vowels."""
    new_str: str = ""
    i: int = 0
    while i < len(a):
        if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u" or i % 3 == 0:
            new_str += a[i]
            i += 1
        if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u" and i % 3 == 0:
            i += 1
    return new_str