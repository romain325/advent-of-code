# 12 red
# 13 green
# 14 blue
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
import array

cnt = 0

def test(balls: array) -> bool:
	for ball in balls:
		res = ball.split(" ")
		if res[1] == "red" and int(res[0]) > 12:
			return False
		if res[1] == "green" and int(res[0]) > 13:
			return False
		if res[1] == "blue" and int(res[0]) > 14:
			return False
	return True


for line in open("input.txt"):
	splitted = line.split(": ")
	id = int(splitted[0].split(" ")[1])

	all_res = True
	for tirage in splitted[1].split("; "):
		res = test(tirage.split(", "))
		all_res = all_res and res

	if all_res:
		print(id)
		cnt += id

print(cnt)
