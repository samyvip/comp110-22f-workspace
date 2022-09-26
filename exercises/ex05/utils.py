"""Building list utility functions."""

__author__ = "730548773"

# from exercises.ex05.utils import

def only_evens(a: list[int]) -> list[int]:
    evens: list = []
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            evens.append(a[i])
        i += 1
    return evens


def concat(a: list[int], b: list[int]) -> list[int]:
    i: int = 0
    while i < len(b):
        a.append(b[i])
        i += 1
    return a


def sub(a: list[int], b: int, c: int) -> list[int]:
    final_list: list = []
    i: int = 0
    if len(a) == 0 or b > len(a) or c <= 0:
        return []
    if b < 0:
        final_list.append(a[i])
    final_list.append(a[b])
    i = b + 1
    while i <= (c - 1) and i < len(a):
        final_list.append(a[i])
        i += 1
    return final_list


