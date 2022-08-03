import array
import functools
import operator


def apply_operation(matrix: array, operation: array):
	m1 = matrix.copy()
	m2 = matrix.copy()
	index = int(operation[1])
	if operation[0] == 'x':
		# horizontal
		for i in range(len(matrix)):
			m1[i] = m1[i][0:index]
			m2[i] = m2[i][index + 1:len(m2[i])]
			m2[i].reverse()
	else:
		# vertical
		m1 = matrix[0:index]
		m2 = matrix[index + 1:len(matrix)]
		m2.reverse()

	for i in range(len(m1)):
		for j in range(len(m1[0])):
			m1[i][j] |= m2[i][j]
	return m1

def pretty_print(arr: array):
	for i in arr:
		for j in i:
			print("#" if j else ".", end="")
		print()

f = open("input2")

input = f.readlines()
indexofmid = input.index('\n')
definitions = [[int(x) for x in i.strip().split(',')] for i in input[0:indexofmid]]
operations = [i.strip().split(" ")[2].split("=") for i in input[indexofmid + 1:len(input)]]

mat = [[False for n in range(max([x[0] for x in definitions]) + 1)] for n2 in range(max([x[1] for x in definitions]) + 1)]
for y, x in definitions:
	mat[x][y] = True

print(len([x for x in functools.reduce(operator.concat,apply_operation(mat, operations[0])) if x]))

m2 = mat.copy()
for op in operations:
	m2 = apply_operation(m2, op)
pretty_print(m2)
