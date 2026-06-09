#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with all values squared."""
    return [[num ** 2 for num in row] for row in matrix]
