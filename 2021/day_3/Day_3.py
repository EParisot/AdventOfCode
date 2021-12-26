INPUT_SIZE = 12

def part_1(data):

	data_tmp = data.copy()
	data_buf = []
	for i in range(INPUT_SIZE):
		s = 0
		data_buf = []
		for d in data_tmp:
			s += int(d[i])
		print(i, s, len(data_tmp) - s, "1" if s >= len(data_tmp) - s else "0")
		for d in data_tmp:
			if (s >= len(data_tmp) - s and d[i] == "1") or (s < len(data_tmp) - s and d[i] == "0"):
				data_buf.append(d)
		data_tmp = data_buf.copy()
		print(data_buf)
		if len(data_buf) == 1:
			ox = int(data_buf[0], 2)
			break
	
	data_tmp = data.copy()
	data_buf = []
	for i in range(INPUT_SIZE):
		s = 0
		data_buf = []
		for d in data_tmp:
			s += int(d[i])
		print(i, s, len(data_tmp) - s, "0" if s >= len(data_tmp) - s else "1")
		for d in data_tmp:
			if (s >= len(data_tmp) - s and d[i] == "0") or (s < len(data_tmp) - s and d[i] == "1"):
				data_buf.append(d)
		data_tmp = data_buf.copy()
		print(data_buf)
		if len(data_buf) == 1:
			co2 = int(data_buf[0], 2)
			break
	
	print(ox, co2, ox * co2)

def part_0(data):
	gamma_str = ["0"] * INPUT_SIZE
	for i in range(INPUT_SIZE):
		s = 0
		for d in data:
			s += int(d[i])
		if s > len(data) - s:
			gamma_str[i] = "1"
	gamma = int("".join(gamma_str), 2)
	epsilon = int("".join(["0" if c == "1" else "1" for c in gamma_str]), 2)
	print(gamma, epsilon, epsilon * gamma)

if __name__ == "__main__":
	with open('input_3.txt') as f:
		data = f.readlines()

	part_0(data)
	part_1(data)