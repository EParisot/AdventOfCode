import numpy as np

def part_0(data):
	med = np.median(data)
	print(med, np.sum(np.abs(data - med)))

def part_1(data):
	grid = []
	m = max(data)
	for i, d in enumerate(data):
		row = []
		for _ in range(m + 1):
			row.append(0)
		grid.append(row)

	for i in range(len(grid)):
		if data[i] + 1 < m:
			grid[i][data[i] + 1] = 1
		for j in range(data[i], m + 1):
			if j - 1 > 0 and grid[i][j - 1]:
				grid[i][j] = grid[i][j - 1] + 1
		for j in range(data[i] + 1, m + 1):
			grid[i][j] += grid[i][j - 1]
				
		if data[i] - 1 >= 0:
			grid[i][data[i] - 1] = 1
		for j in range(data[i] - 1, -1, -1):
			if j + 1 < m and grid[i][j + 1]:
				grid[i][j] = grid[i][j + 1] + 1
		for j in range(data[i] - 1, -1, -1):
			grid[i][j] += grid[i][j + 1]
		
	#for i in range(len(grid)):
	#	print(grid[i])

	col_sums = []
	for j in range(m + 1):
		c_sum = 0
		for i in range(len(grid)):
			c_sum += grid[i][j]
		col_sums.append(c_sum)

	print(col_sums.index(min(col_sums)), min(col_sums))

if __name__ == "__main__":
	data = open("input_7.txt").read().splitlines()
	data = list(map(int, data[0].split(",")))

	part_0(data)
	part_1(data)