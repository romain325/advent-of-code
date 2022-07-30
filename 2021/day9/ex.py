import array


def get_nearby(mat: array, i: int, j: int):
    nb = []
    if i < len(mat) - 1:
        nb.append([i + 1,j])
    if i > 0:
        nb.append([i - 1, j])
    if j > 0:
        nb.append([i, j - 1])
    if j < len(mat[i]) - 1:
        nb.append([i, j + 1])
    return nb


def bassin_size(matrix, x, y, record, r_len, c_len):
    if x < 0 or y < 0 or x > r_len or y > c_len \
            or matrix[x][y] == 9 \
            or (x, y) in record:
        return

    record.append((x, y))

    bassin_size(matrix, x, y + 1, record, r_len, c_len)
    bassin_size(matrix, x, y - 1, record, r_len, c_len)
    bassin_size(matrix, x - 1, y, record, r_len, c_len)
    bassin_size(matrix, x + 1, y, record, r_len, c_len)

f = open("input2")

mat = []
for line in f:
    mat.append([int(i) for i in list(line.strip())])

lowpoints = []

for i in range(len(mat)):
    for j in range(len(mat[i])):
        nearby = get_nearby(mat, i, j)
        if len(list(filter(lambda lamb: mat[lamb[0]][lamb[1]] <= mat[i][j], nearby))) == 0:
            lowpoints.append([i, j])

cnt = 0
for x, y in lowpoints:
    cnt += (mat[x][y] + 1)

print(cnt)

bassin = []
for loc in lowpoints:
    record = []
    bassin_size(mat, loc[0], loc[1], record, len(mat)-1, len(mat[0])-1)
    bassin.append(len(record))

s = sorted(bassin, reverse=True)
print(s[0] * s[1] * s[2])
