def paths_counter_0(data, path, count):
	if path[-1] == "end":
		count += 1
		path.pop()
		return count
	for w in data[path[-1]]:
		if (w.islower() and w not in path) or w.isupper():
			path.append(w)
			count = paths_counter_0(data, path, count)
	path.pop()
	return count

def part_0(data):
	count = paths_counter_0(data, ["start"], 0)
	print(count)

def path_counter_1(data, path, c):
	if path[-1] == "end":
		c += 1
		#print(path)
		path.pop()
		return c
	for w in data[path[-1]]:
		if w != "start" and (w.isupper() or \
		(w.islower() and (not w in path or (path.count(w) == 1 and not any([path.count(x) == 2 if x.islower() else False for x in path]))))):
			path.append(w)
			c = path_counter_1(data, path, c)
	path.pop()
	return c

def part_1(data):
	count = path_counter_1(data, ["start"], 0)
	print(count)

if __name__ == "__main__":
	data = open("input_12.txt").read().splitlines()

	data = [d.split("-") for d in data]
	data_dict = {}
	for d in data:
		if not d[0] in data_dict:
			data_dict[d[0]] = []
		data_dict[d[0]].append(d[1])
		if not d[1] in data_dict:
			data_dict[d[1]] = []
		data_dict[d[1]].append(d[0])

	"""for k, v in data_dict.items():
		print(k, v)
	print()"""

	part_0(data_dict)
	part_1(data_dict)