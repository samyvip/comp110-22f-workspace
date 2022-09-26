"""EX04- List Utility Functions."""

__author__ = "730548773"


def all(a: list[int], b: int) -> bool:
    """Checks whether item is present in list."""
    i: int = 0
    if len(a) == 0:
        return False
    while i < len(a):
        if b != a[i]:
            return False
        i += 1
    return True


def max(a: list[int]) -> int:
    """Identifies the largest number."""
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    new_max: int = a[0]
    while i < len(a):
        if a[i] > new_max:
            new_max = a[i]
        i += 1
    return new_max


def is_equal(a: list[int], b: list[int]) -> bool:
    """Checks for deep equality."""
    i: int = 0
    if len(a) != len(b):
        return False
    if len(a) == 0 and len(b) == 0:
        return True
    while i < len(a):
        if a[i] != b[i]:
            return False
        i += 1
    return True
