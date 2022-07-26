#!/bin/python3

n = 80

f = open("./input1")

# bruteforce

line = f.readline()
arr = [int(i) for i in line.split(",")]


def brute():
    for i in range(n):
        for j in range(len(arr)):
            if arr[j] == 0:
                arr[j] = 6
                arr.append(8)
            else:
                arr[j] -= 1
    print(len(arr))


def smart():
    val = [0] * 9  # zeros arr
    for v in arr:
        val[v] += 1

    for i in range(256):
        current = i % 9
        val[(current + 7) % 9] += val[current]

    print(sum(val))


# brute()

smart()
