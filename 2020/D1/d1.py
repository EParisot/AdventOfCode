with open("input.txt") as f:
	data = f.readlines()

data = list(map(int, data))
for l in data:
	for r in data:
		if l + r == 2020:
			print(l * r)