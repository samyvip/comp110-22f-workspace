"""EX07- Unit Tests for Dictionary Functions."""

__author__ = "730548773"

from dictionary import invert
from dictionary import count
from dictionary import favorite_color


def test_invert_empty() -> None:
    """Edge case: Tests the invert function with an empty list."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_characters() -> None:
    """Use case: Tests whether invert function correctly inverts a dictionary of strings that are characters."""
    xs: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(xs) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_words() -> None:
    """Use case: Tests whether invert function correctly inverts a dictionary of strings that are words."""
    xs: dict[str, str] = {'dog': 'cat', 'love': 'hate', 'mom': 'dad'}
    assert invert(xs) == {'cat': 'dog', 'hate': 'love', 'dad': 'mom'}


def test_favorite_color_empty() -> None:
    """Edge case: Tests the favorite color function with an empty list."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ''
    

def test_favorite_color_normal() -> None:
    """Use case: Tests whether favorite color function correctly outputs the most-occurring color."""
    xs: dict[str, str] = {'John': 'pink', 'Jack': 'black', 'Mary': 'pink'}
    assert favorite_color(xs) == 'pink'


def test_favorite_color_tie() -> None:
    """Use case: Tests whether favorite color function correctly outputs the first-appearing color when there is a tie."""
    xs: dict[str, str] = {'John': 'black', 'Jack': 'black', 'Mary': 'pink', 'Jake': 'pink'}
    assert favorite_color(xs) == 'black'


def test_count_empty() -> None:
    """Edge case: Tests the count function with an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_int() -> None:
    """Use case: Tests the count function with a list of numbers."""
    xs: list[str] = ["1", "6", "7", "9", "10", "9", "5"]
    assert count(xs) == {"1": 1, "6": 1, "7": 1, "9": 2, "10": 1, "5": 1}


def test_count_characters() -> None:
    """Use case: Tests the count function with a list of multiple numbers that occur multiple times."""
    xs: list[str] = ["a", "b", "b", "c", "c"]
    assert count(xs) == {'a': 1, 'b': 2, 'c': 2}