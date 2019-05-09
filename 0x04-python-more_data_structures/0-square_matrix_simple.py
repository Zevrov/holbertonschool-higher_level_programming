#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    eachNewMatrixList = []
    for eachList in matrix:
        for eachNumber in eachList:
            eachNewMatrixList.append(eachNumber ** 2)
        newMatrix.append(eachNewMatrixList)
        eachNewMatrixList = []
    return newMatrix
