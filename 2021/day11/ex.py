import array


def contains_flashing(mat: array) -> bool:
	return 10 in (y for x in mat for y in x)


def get_next_flashing(mat: array) -> array:
	for sub in mat:
		if 10 in sub:
			return [mat.index(sub), sub.index(10)]
	return [-1]


def add_energy_around(mat: array, pos: array):
	mat[pos[0]][pos[1]] = 0
	granted = [[True for i in range(3)] for j in range(3)]
	granted[1][1] = False
	if pos[0] == 0:
		granted[0] = [False] * 3
	if pos[0] == len(mat) - 1:
		granted[2] = [False] * 3
	if pos[1] == 0:
		for i in range(3):
			granted[i][0] = False
	if pos[1] == len(mat[0]) - 1:
		for i in range(3):
			granted[i][2] = False

	for i in range(3):
		for j in range(3):
			if granted[i][j]:
				# print(pos[0] + (i-1), pos[1] + (j-1))
				if not (mat[pos[0] + (i - 1)][pos[1] + (j - 1)] == 0 or
						mat[pos[0] + (i - 1)][pos[1] + (j - 1)] == 10):
					mat[pos[0] + (i - 1)][pos[1] + (j - 1)] += 1


def print_arr(mat: array):
	for i in mat:
		print(' '.join(str(j) for j in i))
	print('\n' * 2)


f = open("input2")

mat = [[int(i) for i in line.strip()] for line in f]
cnt = 0
for i in range(100):
	mat = [[i + 1 for i in line] for line in mat]
	while contains_flashing(mat):
		pos = get_next_flashing(mat)
		if pos[0] == -1:
			break
		add_energy_around(mat, pos)
		cnt += 1

print(cnt)

flag = True
cnt = 0
f.seek(0)
mat = [[int(i) for i in line.strip()] for line in f]
while flag:
	mat = [[i + 1 for i in line] for line in mat]
	while contains_flashing(mat):
		pos = get_next_flashing(mat)
		if pos[0] == -1:
			break
		add_energy_around(mat, pos)
	if all(map(lambda val:  val == 0, (y for x in mat for y in x))):
		flag = False
	cnt += 1

print(cnt)
