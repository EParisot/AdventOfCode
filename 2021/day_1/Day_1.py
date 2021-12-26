def part_1(data):
	res = 0
	prev = None
	for d in data:
		if prev is not None:
			if d > prev:
				res += 1
		prev = d
	print(res)

def part_2(data):
	res = 0
	prev = None
	for i in range(len(data)):
		d = sum(data[i:i+3])
		if prev is not None:
			if d > prev:
				res += 1
		prev = d
	print(res)

if __name__ == '__main__':

	with open('input_1.txt') as f:
		data = f.readlines()
	data = list(map(int, data))

	part_1(data)
	part_2(data)