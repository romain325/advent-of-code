f = open("./input1")

linecnt=0
cnt = []
gamma = epsilon = ""

l = f.readline()
for i in range(len(l.strip())):
    cnt.append(0)


f.seek(0)
for line in f:
    for i, c in enumerate(line.strip()):
        cnt[i] += int(c)
    linecnt += 1

for x in cnt:
    gamma += ("1" if x > linecnt/2 else "0")

epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

print(gamma)
print(epsilon)
print(int(gamma, 2) * int(epsilon, 2))

######################################################################################
f.seek(0)

def cmp(a: int, b: int, c: bool) -> bool:
    if not c:
        return a >= b
    else:
        return a < b

oxygen = 0
c02 = 0
lines = f.readlines()

for entry in range(2):
    res = lines
    linelen = len(lines[0].strip())
    for offset in range(linelen):
        count = 0
        for i in range(len(res)):
            count += int(res[i][offset])
        if cmp(count, len(res)/2, entry):
            res = [line.strip() for line in res if line[offset] == "1"]
        else:
            res = [line.strip() for line in res if line[offset] == "0"]
        if len(res) == 1:
            break
    if entry == 0:
        oxygen = res[0]
    else:
        c02 = res[0]

print(oxygen)
print(c02)
print(int(oxygen, 2) * int(c02, 2))