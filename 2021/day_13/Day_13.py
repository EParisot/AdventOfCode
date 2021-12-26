def part_0(data, fold):

	if fold[0] == "x":
		offset = 0
		for j in range(int(fold[1] + 1), len(data[0])):
			offset += 1
			for i in range(len(data)):
				if data[i][fold[1] - offset] == "#" or data[i][j] == "#":
					data[i][fold[1] - offset] = "#"
				else:
					data[i][fold[1] - offset] = "."
		for i in range(len(data)):
			data[i] = data[i][:fold[1]]
	else:
		offset = 0
		for i in range(fold[1] + 1, len(data)):
			offset += 1
			for j in range(len(data[i])):
				if data[fold[1] - offset][j] == "#" or data[i][j] == "#":
					data[fold[1] - offset][j] = "#"
				else:
					data[fold[1] - offset][j] = "."
		data = data[:fold[1]]

	count = 0
	for i in data:
		#print(i)
		for j in i:
			if j == "#":
				count += 1
	print(count)

def part_1(data, folds):
	for fold in folds:
		if fold[0] == "x":
			offset = 0
			for j in range(int(fold[1] + 1), len(data[0])):
				offset += 1
				for i in range(len(data)):
					if data[i][fold[1] - offset] == "#" or data[i][j] == "#":
						data[i][fold[1] - offset] = "#"
					else:
						data[i][fold[1] - offset] = "."
			for i in range(len(data)):
				data[i] = data[i][:fold[1]]
		else:
			offset = 0
			for i in range(fold[1] + 1, len(data)):
				offset += 1
				for j in range(len(data[i])):
					if data[fold[1] - offset][j] == "#" or data[i][j] == "#":
						data[fold[1] - offset][j] = "#"
					else:
						data[fold[1] - offset][j] = "."
			data = data[:fold[1]]

	for i in data:
		print(i)

if __name__ == "__main__":
	data = open("input_13.txt").read().splitlines()

	cleaned_data = []
	folds = []
	for line in data:
		if "," in line:
			cleaned_data.append(list(map(int, line.split(","))))
		elif line == "":
			pass
		else:
			if "along x" in line:
				folds.append(("x", int(line.split("=")[-1])))
			elif "along y" in line:
				folds.append(("y", int(line.split("=")[-1])))

	grid_max_x = 0
	grid_max_y = 0
	for i in range(len(cleaned_data)):
		if cleaned_data[i][0] > grid_max_x:
			grid_max_x = cleaned_data[i][0]
		if cleaned_data[i][1] > grid_max_y:
			grid_max_y = cleaned_data[i][1]
	grid = []
	for i in range(grid_max_y+1):
		line = []
		for j in range(grid_max_x+1):
			if [j, i] in cleaned_data:
				line.append("#")
			else:
				line.append(".")
		grid.append(line)

	part_0(grid.copy(), folds[0])
	part_1(grid.copy(), folds)