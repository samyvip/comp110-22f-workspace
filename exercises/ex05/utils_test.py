"""Testing list utility functions."""

__author__ = "730548773"

from utils import only_evens
from utils import concat
from utils import sub


def test_only_evens_empty() -> None:
    """Tests the only_evens function with an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_evens() -> None:
    """Tests the only_evens function with a list of even numbers."""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_odds() -> None:
    """Tests the only_evens function with a lost of odd numbers."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_concat_empty() -> None:
    """Tests the concat function with an empty list."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_consecutive() -> None:
    """Tests the concat function with a list of consecutive numbers."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_nonconsecutive() -> None:
    """Tests the concat function with a list of non-consecutive numbers."""
    xs: list[int] = [1, 4, 6]
    ys: list[int] = [3, 7, 10]
    assert concat(xs, ys) == [1, 4, 6, 3, 7, 10]


def test_sub_empty() -> None:
    """Tests the sub function with an empty list."""
    a_list: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == []


def test_sub_start_index_one() -> None:
    """Tests the sub function with a start index of one."""
    a_list: list[int] = [59, 60, 37, 45, 62]
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == [60, 37, 45]


def test_sub_start_index_greater() -> None:
    """Tests the sub function with a start index greater than one."""
    a_list: list[int] = [2, 57, 89, 45, 60, 73, 95, 67]
    start: int = 3
    end: int = 7
    assert sub(a_list, start, end) == [45, 60, 73, 95]