def part_0(data):
	for i in range(80):
		data_cpy = data.copy()
		for j, n in enumerate(data_cpy):
			if n == 0:
				data[j] = 6
				data.append(8)
			else:
				data[j] -= 1
	print(len(data))

def part_1(data):
	data_dict = {n: 0 for n in range(9)}
	for d in data:
		data_dict[d] += 1
	for i in range(256):
		mem8 = data_dict[8]
		mem6 = data_dict[6]
		data_dict[8] = data_dict[0]
		data_dict[6] = data_dict[0]
		data_dict[0] = data_dict[1]
		data_dict[1] = data_dict[2]
		data_dict[2] = data_dict[3]
		data_dict[3] = data_dict[4]
		data_dict[4] = data_dict[5]
		data_dict[5] = mem6
		data_dict[6] += data_dict[7]
		data_dict[7] = mem8
	print(sum(data_dict.values()))

if __name__ == "__main__":
	data = open("input_6.txt").read().splitlines()[0]
	data = list(map(int, data.split(",")))

	part_0(data.copy())
	part_1(data.copy())

	