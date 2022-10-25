"""Dictionary related utility functions."""

__author__ = "730548773"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(list_of_rows: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list of str of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in list_of_rows:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(list_of_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = list_of_rows[0]
    for column in first_row:
        result[column] = column_values(list_of_rows, column)
    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with the first N rows of data for each column."""
    result: dict = {}
    for column in column_table:
        first_n_values: list = []
        i: int = 0
        while i < rows:
            first_n_values.append(column_table[column][i])
            i += 1
        result[column] = first_n_values
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only a subset of the original columns."""
    result: dict = {}
    for column in column_names:
        result[column] = column_table[column]
    return result


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-based table with two column-based tables combined."""
    result: dict = {}
    for column in column_table_1:
        result[column] = column_table_1[column]
    for column in column_table_2:
        if column in result:
            result[column] += column_table_2[column]
        else:
            result[column] = column_table_2[column]
    return result


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a value occurs in a list."""
    final: dict[str, int] = {}
    for item in a:
        if item in final:
            final[item] += 1
        else:
            final[item] = 1
    return final