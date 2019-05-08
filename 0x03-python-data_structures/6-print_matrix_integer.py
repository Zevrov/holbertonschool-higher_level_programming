#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	for y in matrix:
		for x in matrix[y]:
			print('{:d}'.format(matrix[y][x]), end='')
			if x != len(matrix[y]) - 1:
				print(' ', end='')
		print('\n', end='')
