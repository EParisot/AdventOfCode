def hex_to_bin(hex_string):
	res = ""
	for i in hex_string:
		res += bin(int(i, 16))[2:].zfill(4)
	return res

def bin_to_int(bin_string):
	return int(bin_string, 2)

packets = []
def read_packet(bin_str, i, packet):
	packets.append(packet)
	if len(packet) == 0:
		packet.append(bin_str[i:i+3])
		i += 3
	if len(packet) == 1:
		packet.append(bin_str[i:i+3])
		i += 3
	if len(packet) == 2 and packet[1] == "100":
		value = []
		while True:
			if bin_str[i] == "1":
				i += 1
				value.append(bin_str[i:i+4])
				i += 4
			elif bin_str[i] == "0" and len(bin_str) - i + 5 > 0:
				i += 1
				value.append(bin_str[i:i+4])
				i += 4
				break
			else:
				break
		packet.append(value)
	elif len(packet) == 2 and packet[1] != "100":
		if bin_str[i] == "0":
			i += 1
			l = bin_to_int(bin_str[i:i+15])
			i += 15
			return read_packet(bin_str, i, [])
		else:
			i += 1
			l = bin_to_int(bin_str[i:i+11])
			i += 11
			return read_packet(bin_str, i, [])

	return packet, i

def part_0(data):
	bin_str = hex_to_bin(data)
	packet = []
	i = 0
	while True:
		packet, i = read_packet(bin_str, i, packet)
		packet = []
		while i < len(bin_str) and all([c == "0" for c in bin_str[i:]]):
			i += 1
		if i >= len(bin_str):
			break

	res = []
	for packet in packets:
		if len(packet) >= 2:
			if len(packet[0]) == 3:
				res.append(packet[0])
			for p in packet:
				if len(p) == 3:
					if len(p[0]) == 3:
						res.append(p[0])

	tot = 0
	for r in res:
		tot += int(r, 2)
	print(tot)

def part_1(data):
	bin_str = hex_to_bin(data)
	packet = []
	i = 0
	while True:
		packet, i = read_packet(bin_str, i, packet)
		packet = []
		while i < len(bin_str) and all([c == "0" for c in bin_str[i:]]):
			i += 1
		if i >= len(bin_str):
			break

	def product(l):
		res = 1
		for i in l:
			res *= i
		return res

	def greater(l, r):
		return int(l > r)

	def less(l, r):
		return int(l < r)
	
	def equal(l, r):
		return int(l == r)

	fcts = [
		sum,
		product,
		min,
		max,
		None,
		greater,
		less,
		equal
	]


if __name__ == "__main__":
	data = open("test_input_16.txt").read().splitlines()

	part_0(str(data[0]))
	packets = []
	part_1(str(data[0]))