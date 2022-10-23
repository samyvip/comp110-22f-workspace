"""EX07- Dictionary Functions."""

__author__ = "730548773"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result:
            raise KeyError("same key encountered again")
        else:
            result[a[key]] = key
    return result


def favorite_color(a: dict[str, str]) -> str:
    """Identifies most frequently occurring color."""
    result: dict[str, int] = {}
    fav_color: str = ""
    for name in a:
        if a[name] in result:
            result[a[name]] += 1
        else:
            result[a[name]] = 1
    max: int = 0
    for color in result:
        current_color: int = result[color]
        if current_color > max:
            max = current_color
            fav_color = color
    return fav_color


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a value occurs in a list."""
    final: dict[str, int] = {}
    for item in a:
        if item in final:
            final[item] += 1
        else:
            final[item] = 1
    return final