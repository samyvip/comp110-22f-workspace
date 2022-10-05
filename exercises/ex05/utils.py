"""Building list utility functions."""

__author__ = "730548773"


def only_evens(a: list[int]) -> list[int]:
    """Returns a list of only even inputs."""
    evens: list[int] = []
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            evens.append(a[i])
        i += 1
    return evens


def concat(a: list[int], b: list[int]) -> list[int]:
    """Generates a new list that includes all of the elements of the first list followed by all of the elements of the second list."""
    new_list: list[int] = []
    i: int = 0
    while i < len(a):
        new_list.append(a[i])
        i += 1
    i: int = 0
    while i < len(b):
        new_list.append(b[i])
        i += 1
    return new_list


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Returns a list that is a subset of the given list between the specified start index and the second-to-last end index."""
    final_list: list[int] = []
    i: int = 0
    if len(a) == 0 or b >= len(a) or c <= 0:
        return []
    if b > 0:
        final_list.append(a[b])
        i = b + 1
        while i <= (c - 1) and i < len(a):
            final_list.append(a[i])
            i += 1
        return final_list
    else:
        final_list.append(a[0])
        i = 1
        while i <= (c - 1) and i < len(a):
            final_list.append(a[i])
            i += 1
        return final_list