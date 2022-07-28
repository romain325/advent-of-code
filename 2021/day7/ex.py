#!/bin/python3
from functools import reduce


def median(l):
	half = len(l) // 2
	l.sort()
	if not len(l) % 2:
		return (l[half - 1] + l[half]) / 2.0
	return l[half]


f = open("./input1")
pos = [int(i) for i in f.readline().split(",")]
med = median(pos)
cost = 0
for c in pos:
	cost += abs(c-med)
print(int(cost))

m = round(sum(pos) / len(pos))
print(str(m) + " mean")
cost = cost2 = 0.0
for c in pos:
	val = abs(m-c)
	s = sum([i for i in range(val +1)])
	cost2 += s
	cost += int(sum([val*(val+1)//2 for i in pos]))
print((cost/1000)-1)
print(cost2-1)


