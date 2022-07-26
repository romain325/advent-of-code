#!/bin/python3
import array
import re
import numpy as np


def points_between(x1, y1, x2, y2):
	d0 = x2 - x1
	d1 = y2 - y1
	count = max(abs(d1), abs(d0))+1
	if d0 == 0:
		return (
			np.full(count, x1),
			np.round(np.linspace(y1, y2, count)).astype(np.int32)
		)
	if d1 == 0:
		return (
			np.round(np.linspace(x1, x2, count)).astype(np.int32),
			np.full(count, y1),
		)
	return (
		np.round(np.linspace(x1, x2, count)).astype(np.int32),
		np.round(np.linspace(y1, y2, count)).astype(np.int32))


def print_mask(mask: array):
	for row in mask:
		for val in row:
			print("." if val == 0 else val, end="")
		print("")


f = open("./input1")
mask = [[0 for j in range(1000)] for i in range(1000)]
maskDiag = [[0 for j in range(1000)] for i in range(1000)]


for line in f:
	result = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
	if result is None or len(result.groups()) <= 1:
		break
	pos1 = [int(result.group(1)), int(result.group(2))]
	pos2 = [int(result.group(3)), int(result.group(4))]
	res = points_between(pos1[0], pos1[1], pos2[0], pos2[1])
	for i in range(len(res[0])):
		if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
			mask[res[1][i]][res[0][i]] += 1
		maskDiag[res[1][i]][res[0][i]] += 1


##print_mask(mask)

print(sum(val > 1 for val in np.array(mask).flatten()))
print(sum(val > 1 for val in np.array(maskDiag).flatten()))
