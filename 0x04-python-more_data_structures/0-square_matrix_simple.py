#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
for eachList in matrix:
	for eachNumber in eachList:
		matrix.append(square(eachNumber))
			return matrix

def square(x):
	x ** 2
	return x
