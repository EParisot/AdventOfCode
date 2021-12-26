def check_bingos_0(bingos):
	for i, bingo in enumerate(bingos):
		for l in bingo:
			if l == [1, 1, 1, 1, 1]:
				return i
		for r in range(5):
			if bingo[0][r] == bingo[1][r] == bingo[2][r] == bingo[3][r] == bingo[4][r] == 1:
				return i
	return -1

def part_0(rnd_nbs, grids):
	bingos = []
	for grid in grids:
		bingos.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
	for nb in rnd_nbs:
		for i, grid in enumerate(grids):
			for j, line in enumerate(grid):
				if nb in line:
					bingos[i][j][line.index(nb)] = 1
		winner = check_bingos_0(bingos)
		if winner > -1:
			score = 0
			for j, l in enumerate(bingos[winner]):
				for k, c in enumerate(l):
					if c == 0:
						score += grids[winner][j][k]
			print(winner, score, nb, score * nb)
			return 

def check_bingos_1(bingos, winners, nb):
	for i, bingo in enumerate(bingos):
		if i in [w[0] for w in winners]:
			continue
		for l in bingo:
			if l == [1, 1, 1, 1, 1]:
				winners.append((i, nb))
		if i in [w[0] for w in winners]:
			continue
		for r in range(5):
			if bingo[0][r] == bingo[1][r] == bingo[2][r] == bingo[3][r] == bingo[4][r] == 1:
				winners.append((i, nb))
	return winners

def part_1(rnd_nbs, grids):
	bingos = []
	winners = []
	for grid in grids:
		bingos.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
	for nb in rnd_nbs:
		for i, grid in enumerate(grids):
			for j, line in enumerate(grid):
				if nb in line:
					bingos[i][j][line.index(nb)] = 1
		winners = check_bingos_1(bingos, winners, nb)
		if len(winners) == len(grids):
			break
	score = 0
	winner = winners[-1][0]
	nb = winners[-1][1]
	for j, l in enumerate(bingos[winner]):
		for k, c in enumerate(l):
			if c == 0:
				score += grids[winner][j][k]
	print(winner, score, nb, score * nb)
	return 

if __name__ == "__main__":
	with open("input_4.txt") as f:
		data = f.read().splitlines()
	
	rnd_nbs = list(map(int, data[0].split(',')))
	raw_grids = data[2::]
	grids = []
	grid = []
	for i, l in enumerate(raw_grids):
		if l == "":
			grids.append(grid)
			grid = []
		else:
			grid.append(list(map(int, l.split())))
	grids.append(grid)
	
	part_0(rnd_nbs, grids)
	part_1(rnd_nbs, grids)