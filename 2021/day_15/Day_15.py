from timeit import default_timer as timer
import heapq

FOUND = -42
MAX = 1000000

class Node():
	def __init__(self, x, y, cost, heuristic):
		self.x = x
		self.y = y
		self.cost = cost
		self.heuristic = heuristic
		self.parent = None
	
	def __lt__(self, other):
		return self.cost + self.heuristic < other.cost + other.heuristic
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash((self.x, self.y))

	def neighbors(self, data):
		n = []
		for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
			if 0 <= self.x + dx < len(data[0]) and 0 <= self.y + dy < len(data):
				n.append(Node(self.x + dx, self.y + dy, self.cost, self.heuristic))
		return n

def debug(data, path):
	total_cost = 0
	for pos in path[1:]:
		total_cost += int(data[pos.y][pos.x])
	for p in path:
		data[p.y] = list(data[p.y])
		data[p.y][p.x] = 'X'
	for i, r in enumerate(data):
		print("".join(r))
	print(total_cost, end="\n")

def heuristic(curr, end):
	return abs(curr.x - end.x) + abs(curr.y - end.x)

def next_cost(next, data):
	return int(data[next.y][next.x])

# IDA Star
def search(curr, cost, thres, data, end, path):
	f = cost + curr.heuristic
	if f > thres:
		return f
	if curr == end:
		debug(data, path)
		return FOUND
	m = MAX
	for node in curr.neighbors(data):
		if not node in path:
			path.append(node)
			tmp = search(node, cost + next_cost(node, data), thres, data, end, path)
			if tmp == FOUND:
				return FOUND
			if tmp < m:
				m = tmp
			path.pop()
	return m

def ida_star(data):
	end = Node(len(data[0]) - 1, len(data) - 1, 0, 0)
	curr = Node(0, 0, 0, 0)
	curr.heuristic = heuristic(curr, end)
	path = [curr]
	thres = curr.heuristic
	while True:
		tmp = search(curr, 0, thres, data, end, path)
		if tmp == FOUND:
			return
		if tmp > MAX:
			print("failed")
			return
		thres = tmp

# A Star
def reconstruct_path(node):
	path = [node]
	while node.parent:
		path.append(node.parent)
		node = node.parent
	return list(reversed(path))

def a_star(data):
	end = Node(len(data[0]) - 1, len(data) - 1, 0, 0)
	curr_node = Node(0, 0, 0, 0)
	curr_node.heuristic = heuristic(curr_node, end)
	open_set = [curr_node]
	heapq.heapify(open_set)
	closed_set = set()

	while len(open_set):
		curr_node = heapq.heappop(open_set)
		if curr_node == end:
			path = reconstruct_path(curr_node)
			debug(data, path)
			return
		for n in curr_node.neighbors(data):
			if n in closed_set or (n in open_set and open_set[open_set.index(n)].cost < n.cost):
				continue
			n.cost = curr_node.cost + next_cost(n, data)
			n.heuristic = heuristic(n, end)
			n.parent = curr_node
			heapq.heappush(open_set, n)
		closed_set.add(curr_node)
	print("ERROR")

# Djikstra (Astar with heuristic -> 0)
def djikstra(data):
	end = Node(len(data[0]) - 1, len(data) - 1, 0, 0)
	curr_node = Node(0, 0, 0, 0)
	open_set = [curr_node]
	heapq.heapify(open_set)
	closed_set = set()

	while len(open_set):
		curr_node = heapq.heappop(open_set)
		if curr_node == end:
			path = reconstruct_path(curr_node)
			debug(data, path)
			return
		for n in curr_node.neighbors(data):
			if n in closed_set or n in open_set:
				continue
			n.cost = curr_node.cost + next_cost(n, data)
			n.parent = curr_node
			heapq.heappush(open_set, n)
		closed_set.add(curr_node)
	print("ERROR")


def part_0(data):
	start = timer()
	djikstra(data.copy())
	end = timer()
	print("Djikstra's Time:", end - start)

	start = timer()
	a_star(data.copy())
	end = timer()
	print("A_Star's Time:", end - start)
	
	"""start = timer()
	ida_star(data.copy())
	end = timer()
	print("IDA_Star's Time:", end - start)"""


def part_1(data):
	l = len(data)

	for i, row in enumerate(data):
		to_append = []
		for r in range(1, 5):
			for j, c in enumerate(row):
				if int(c) + r <= 9:
					to_append.append(str(int(c) + r))
				else:
					to_append.append(str(int(c) + r - 9))
		data[i] += "".join(to_append)

	for r in range(1, 5):
		for i, row in enumerate(data[:l]):
			to_append = []
			for j, c in enumerate(row):
				if int(c) + r <= 9:
					to_append.append(str(int(c) + r))
				else:
					to_append.append(str(int(c) + r - 9))
			data.append("".join(to_append))
	"""for r in data:
		print(r)"""
	part_0(data)

	for r in data:
		print(r)

if __name__ == "__main__":
	data = open("input_15.txt").read().splitlines()

	part_0(data.copy())
	part_1(data.copy())