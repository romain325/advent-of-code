#!/bin/python3

n = 80

f = open("./input1")
line = f.readline()
arr = [int(i) for i in line.split(",")]


for i in range(n):
    for j in range(len(arr)):
        if arr[j] == 0:
            arr[j] = 6
            arr.append(8)
        else:
            arr[j] -= 1

print(len(arr))