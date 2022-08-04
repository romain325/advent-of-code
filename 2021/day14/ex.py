from collections import defaultdict

f = open("input2")

template = list(f.readline().strip())
restL = [n.strip().split(" -> ") for n in f.readlines()[1:]]
rest = {}
for x, y in restL:
	rest[x] = y


def find_polymer(polymer: list) -> str:
	to_insert = []
	for i in range(len(polymer) - 1):
		if polymer[i] + polymer[i + 1] in rest:
			to_insert.append(
				[rest[polymer[i] + polymer[i + 1]], i + len(to_insert) + 1])

	for new_letter in to_insert:
		polymer.insert(new_letter[1], new_letter[0])
	return ''.join(polymer)


v1 = ''.join(template.copy())
for i in range(10):
	v1 = find_polymer(list(v1))

cnt = defaultdict(lambda: 0)
for c in v1:
	cnt[c] += 1
print(max(cnt.values()) - min(cnt.values()))


def find_polymer2(polymer: dict) -> dict:
	new_polymer = polymer.copy()
	for ke in polymer:
		middle = rest.get(ke)
		if middle == 0:
			continue
		new_polymer[ke] -= polymer[ke]
		for key in [ke[0] + middle, middle + ke[1]]:
			new_polymer[key] += polymer[ke]
	return defaultdict(lambda: 0, new_polymer)


entry = defaultdict(lambda: 0)
for c in range(len(template) - 1):
	entry[template[c] + template[c + 1]] += 1

for i in range(40):
	entry = find_polymer2(entry)

cnt = defaultdict(lambda: 0)
for k in entry:
	cnt[k[0]] += entry[k]
	cnt[k[1]] += entry[k]

cnt[template[0]] += 1
cnt[template[len(template)-1]] += 1
test = [[k, cnt[k] // 2] for k in cnt]
print(max([row[1] for row in test]) - min([row[1] for row in test]))
