"""EX04- List Utility Functions."""

__author__ = "730548773"

def all(a: list[int], b: int) -> bool:
    i: int = 0
    while i < len(a):
        if b != a[i]:
            return False
        i += 1
    return True

def max(a: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    new_max: int = 0
    while i < len(a):
        if a[i] > new_max:
            new_max = a[i]
        i += 1
    return new_max

def is_equal(a: list[int], b: list[int]) -> bool:
    i: int = 0
    while i < len(a) and len(b):
        if a[i] != b[i]:
            return False
        i += 1
    return True
