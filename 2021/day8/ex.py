#!/bin/python3
import array
import string

import numpy as np

def get_mid_char(letter: string, candidates: array):
	for c in letter:
		if len([c for x in candidates if c not in x]):
			return c

f = open("./input1")
cnt = 0
for line in f:
	out_values = line.strip().split(" | ")[1].split(" ")
	cnt += len(list(filter(lambda x: len(x) in [2,3,4,7], out_values)))
print(cnt)

cnt = 0
known_length = {
	2: 1,
	4: 4,
	3: 7,
	7: 8,
}

f.seek(0)
for line in f:
	solved = {}
	[in_v, out_v] = [x.split(" ") for x in line.strip().split(" | ")]
	in_v = [''.join(sorted(x)) for x in in_v]
	out_v = [''.join(sorted(x)) for x in out_v]

	# solve all 1,4,7,8 digits
	for i in in_v:
		try:
			solved[known_length[len(i)]] = i
		except KeyError:
			pass

	# solve 2,5,6
	# put against 1 -> 2 will have lower, 6 none and 5 upper
	[firstC, sndC] = solved[1]
	candidates = [[s for s in in_v if firstC in s and sndC not in s], [s for s in in_v if sndC in s and firstC not in s]]
	solved[2] = min(candidates, key=len)[0]
	solved[5] = str(min(max(candidates, key=len), key=len))
	solved[6] = str(max(max(candidates, key=len), key=len))

	# solve 0,3,9
	# get not resolved one, 3 is smallest
	# find central char & deducte 9
	candidates = [s for s in in_v if s not in list(solved.values())]
	solved[3] = str(min(candidates, key=len))
	del candidates[candidates.index(min(candidates, key=len))]
	# find mid bar char from 4
	mid_char = get_mid_char(solved[4], candidates)
	solved[9] = [s for s in candidates if mid_char in s][0]
	solved[0] = [s for s in candidates if mid_char not in s][0]

	# everything solved! create output
	val = list(solved.values())
	keys = list(solved.keys())
	result = ""
	for o in out_v:
		result += str(keys[val.index(o)])
	cnt += int(result)

print(cnt)

