# 12 red
# 13 green
# 14 blue
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
import array

cnt = 0


def get_arr(balls: array) -> array:
	test = [0, 0, 0]
	for ball in balls:
		res = ball.split(" ")
		print(res)
		if res[1] == "red":
			test[0] = int(res[0])
		if res[1] == "green":
			test[1] = int(res[0])
		if res[1] == "blue":
			test[2] = int(res[0])
	return test


for line in open("input.txt"):
	splitted = line.strip().split(": ")
	id = int(splitted[0].split(" ")[1])

	all_res = [0,0,0]
	for tirage in splitted[1].split("; "):
		res = get_arr(tirage.split(", "))
		for i in range(3):
			if res[i] > all_res[i]:
				all_res[i] = res[i]

	precnt = 1
	print(all_res)
	for i in range(3):
		if all_res[i] > 0:
			precnt *= all_res[i]
	print(precnt)
	cnt += precnt

print(cnt)
