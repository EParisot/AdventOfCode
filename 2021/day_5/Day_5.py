def draw_line_0(grid, points):
	x1, y1, x2, y2 = points
	if x1 == x2:
		if y1 > y2:
			for i in range(y2, y1+1):
				grid[i][x1] += 1
		else:
			for i in range(y1, y2+1):
				grid[i][x1] += 1
	elif y1 == y2:
		if x1 > x2:
			for i in range(x2, x1+1):
				grid[y1][i] += 1
		else:
			for i in range(x1, x2+1):
				grid[y1][i] += 1
	#else:
	#	print("Error")
	return grid

def part_0(data):
	grid_size = 10
	all_points = []
	for line in data:
		points = line.split(" -> ")
		x1, y1 = list(map(int, points[0].split(",")))
		x2, y2 = list(map(int, points[1].split(",")))
		all_points.append((x1, y1, x2, y2))
		if max((x1, y1, x2, y2)) + 1 > grid_size:
			grid_size = max((x1, y1, x2, y2)) + 1
	grid = []
	for i in range(grid_size):
		line = []
		for j in range(grid_size):
			line.append(0)
		grid.append(line)
	for points in all_points:
		grid = draw_line_0(grid, points)
	
	print(sum(y >= 2 for x in grid for y in x))
	#for l in grid:
	#	print(l)

def draw_line_1(grid, points):
	x1, y1, x2, y2 = points
	if x1 == x2:
		if y1 > y2:
			for i in range(y2, y1+1):
				grid[i][x1] += 1
		else:
			for i in range(y1, y2+1):
				grid[i][x1] += 1
	elif y1 == y2:
		if x1 > x2:
			for i in range(x2, x1+1):
				grid[y1][i] += 1
		else:
			for i in range(x1, x2+1):
				grid[y1][i] += 1
	else:
		if x1 < x2:
			if y1 < y2:
				for i in range(x2 - x1 + 1):
					grid[y1+i][x1+i] += 1
			else:
				for i in range(x2 - x1 + 1):
					grid[y1-i][x1+i] += 1
		else:
			if y1 < y2:
				for i in range(x1 - x2 + 1):
					grid[y2-i][x2+i] += 1
			else:
				for i in range(x1 - x2 + 1):
					grid[y2+i][x2+i] += 1
	return grid

def part_1(data):
	grid_size = 10
	all_points = []
	for line in data:
		points = line.split(" -> ")
		x1, y1 = list(map(int, points[0].split(",")))
		x2, y2 = list(map(int, points[1].split(",")))
		all_points.append((x1, y1, x2, y2))
		if max((x1, y1, x2, y2)) + 1 > grid_size:
			grid_size = max((x1, y1, x2, y2)) + 1
	grid = []
	for i in range(grid_size):
		line = []
		for j in range(grid_size):
			line.append(0)
		grid.append(line)
	for points in all_points:
		grid = draw_line_1(grid, points)
	
	print(sum(y >= 2 for x in grid for y in x))
	#for l in grid:
	#	print(l)

if __name__ == "__main__":
	with open("input_5.txt") as f:
		data = f.readlines()

	part_0(data)
	part_1(data)