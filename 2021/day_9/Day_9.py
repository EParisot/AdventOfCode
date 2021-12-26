def part_0(data):
	mins = []
	for i, r in enumerate(data):
		for j, c in enumerate(r):
			if ((i - 1 >= 0 and c < data[i-1][j]) or i - 1 < 0) and \
				((j - 1 >= 0 and c < data[i][j-1]) or j - 1 < 0) and \
				((i + 1 < len(data) and c < data[i+1][j]) or i + 1 >= len(data)) and \
				((j + 1 < len(r) and c < data[i][j+1]) or j + 1 >= len(r)):
				mins.append(int(c))
	print(sum([r + 1 for r in mins]))

def check_pos(x, y, val, to_check, checked, bassin):
	if y - 1 >= 0:
		if (not (x, y-1, int(data[y-1][x])) in checked or (val < int(data[y-1][x]) and not (x, y-1, int(data[y-1][x])) in bassin)) and \
		int(data[y-1][x]) < 9 and val < int(data[y-1][x]):
			to_check.append((x, y-1, int(data[y-1][x])))
			bassin.append((x, y-1, int(data[y-1][x])))
		checked.append((x, y-1, int(data[y-1][x])))
	if x - 1 >= 0:
		if (not (x-1, y, int(data[y][x-1])) in checked or (val < int(data[y][x-1]) and not (x-1, y, int(data[y][x-1])) in bassin)) and \
		int(data[y][x-1]) < 9 and val < int(data[y][x-1]):
			to_check.append((x-1, y, int(data[y][x-1])))
			bassin.append((x-1, y, int(data[y][x-1])))
		checked.append((x-1, y, int(data[y][x-1])))
	if y + 1 < len(data):
		if (not (x, y+1, int(data[y+1][x])) in checked or (val < int(data[y+1][x]) and not (x, y+1, int(data[y+1][x])) in bassin)) and \
		int(data[y+1][x]) < 9 and val < int(data[y+1][x]):
			to_check.append((x, y+1, int(data[y+1][x])))
			bassin.append((x, y+1, int(data[y+1][x])))
		checked.append((x, y+1, int(data[y+1][x])))
	if x + 1 < len(data[0]):
		if (not (x+1, y, int(data[y][x+1])) in checked or (val < int(data[y][x+1]) and not (x+1, y, int(data[y][x+1])) in bassin)) and \
		int(data[y][x+1]) < 9 and val < int(data[y][x+1]):
			to_check.append((x+1, y, int(data[y][x+1])))
			bassin.append((x+1, y, int(data[y][x+1])))
		checked.append((x+1, y, int(data[y][x+1])))
	to_check.remove((x, y, val))
	return to_check, checked, bassin

def part_1(data):
	mins = []
	for i, r in enumerate(data):
		for j, c in enumerate(r):
			if ((i - 1 >= 0 and c < data[i-1][j]) or i - 1 < 0) and \
				((j - 1 >= 0 and c < data[i][j-1]) or j - 1 < 0) and \
				((i + 1 < len(data) and c < data[i+1][j]) or i + 1 >= len(data)) and \
				((j + 1 < len(r) and c < data[i][j+1]) or j + 1 >= len(r)):
				mins.append((j, i, int(c)))
	bassins = []
	for m in mins:
		size = 0
		x, y = m[0], m[1]
		val = m[2]
		bassin = [(x, y, val)]
		to_check = []
		checked = []
		to_check.append((x, y, val))
		while len(to_check):
			x, y, val = to_check[0]
			to_check, checked, bassin = check_pos(x, y, val, to_check, checked, bassin)
			size += 1
		bassins.append((size, bassin))
		"""print((size, bassin))
		tests = []
		for i in range(len(data)):
			test = []
			for j in range(len(data[0])):
				test.append(0)
			tests.append(test)
		for b in bassin:
			tests[b[1]][b[0]] = b[2]
		for t in tests:
			print(t)"""
	top_bassins = sorted(bassins, key=lambda x: x[0], reverse=True)
	res = 1
	for t in top_bassins[:3]:
		res *= t[0]
	print(res)

if __name__ == "__main__":
	data = open("input_9.txt").read().splitlines()

	part_0(data)
	part_1(data)