def print_data(data):
	for i in range(len(data)):
		print(data[i])
	print()

flashed = []
def flash(i, j, data):
	if data[i][j] == 0:
		return
	data[i][j] = 0
	flashed.append((i, j))
	for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)):
		if 0 <= x < len(data) and 0 <= y < len(data[0]):
			if data[x][y] == 0 and (x, y) in flashed:
				continue
			data[x][y] += 1
			if data[x][y] > 9:
				flash(x, y, data)
	return

def part_0(data):
	result = 0
	global flashed
	for r in range(100):
		flashed = []
		for i in range(len(data)):
			for j in range(len(data[i])):
				if data[i][j] == 0 and (i, j) in flashed:
					continue
				data[i][j] += 1
				if data[i][j] > 9:
					flash(i, j, data)
		result += len(flashed)		
	print(result)

def part_1(data):
	result = 0
	global flashed
	while True:
		flashed = []
		for i in range(len(data)):
			for j in range(len(data[i])):
				if data[i][j] == 0 and (i, j) in flashed:
					continue
				data[i][j] += 1
				if data[i][j] > 9:
					flash(i, j, data)
		result += 1
		if all(data[i][j] == 0 for i in range(len(data)) for j in range(len(data[i]))):
			break
	print(result)

if __name__ == "__main__":
	source_data = open("test_input_11.txt").read().splitlines()

	part_0([[int(x) for x in line] for line in source_data])
	part_1([[int(x) for x in line] for line in source_data])
	