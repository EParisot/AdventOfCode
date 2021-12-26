def apply_forces(pos, velocities):
	pos[0] += velocities[0]
	pos[1] += velocities[1]
	if velocities[0] != 0:
		if pos[0] > 0:
			velocities[0] -= 1
		elif pos[0] < 0:
			velocities[0] += 1
	velocities[1] -= 1
	return pos, velocities

def part_0(data):

	velocities = []
	pos = [0, 0]

	paths = []
	for i in range(1000, 0, -1):
		for j in range(1000, 0, -1):
			orig_velocities = [j, i]
			velocities = [j, i]
			pos = [0, 0]
			path = []
			while True:
				pos, velocities = apply_forces(pos, velocities)
				path.append(pos.copy())
				if min(data[0]) <= pos[0] <= max(data[0]) and min(data[1]) <= pos[1] <= max(data[1]):
					paths.append((orig_velocities, path))
					break
				elif pos[0] > max(data[0]) or pos[1] < min(data[1]):
					break
	
	max_y = 0
	min_x = 1000000
	best_path = None
	best_v = None
	for v, path in paths:
		for p in path:
			if p[1] >= max_y and p[0] <= min_x:
				max_y = p[1]
				best_path = path
				best_v = v
	
	print(best_v, max(best_path, key=lambda x: x[1])[1])
				

def part_1(data):
	velocities = []
	pos = [0, 0]

	paths = []
	for i in range(-1000, 1000):
		for j in range(1000, 0, -1):
			orig_velocities = [j, i]
			velocities = [j, i]
			pos = [0, 0]
			path = []
			while True:
				pos, velocities = apply_forces(pos, velocities)
				path.append(pos.copy())
				if min(data[0]) <= pos[0] <= max(data[0]) and min(data[1]) <= pos[1] <= max(data[1]):
					paths.append((orig_velocities, path))
					break
				elif pos[0] > max(data[0]) or pos[1] < min(data[1]):
					break

	print(len(paths))

if __name__ == "__main__":
	data = open("input_17.txt").read().splitlines()

	d = data[0].split("=")
	x_lims = list(map(int, d[1].split(",")[0].split("..")))
	y_lims = list(map(int, d[2].split("..")))

	part_0((x_lims, y_lims))
	part_1((x_lims, y_lims))