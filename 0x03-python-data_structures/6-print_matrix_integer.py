#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for sub in matrix:
        if len(sub) == 0:
            print()

        for index in range(len(sub)):
            print("{:d}".format(sub[index]),
                  end="\n" if index is len(sub) - 1 else " ")
