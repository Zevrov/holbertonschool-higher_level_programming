#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda answer: list(map(lambda i: i**2, answer)), matrix))
