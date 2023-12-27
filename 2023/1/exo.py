import re

cnt = 0

for line in open("input.txt"):
	line = re.sub(r'\D', '', line)
	nb = int(line[0]) *10 + int(line[-1])
	cnt += nb
print(cnt)
