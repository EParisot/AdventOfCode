def part_0(data):
	x = 0
	y = 0

	for d in data:
		cmd = d.split()
		if cmd[0] == "forward":
			x += int(cmd[1])
		elif cmd[0] == "up":
			y -= int(cmd[1])
		else:
			y += int(cmd[1])

	print(x * y)

def part_1(data):
	x = 0
	y = 0
	aim = 0

	for d in data:
		cmd = d.split()
		if cmd[0] == "forward":
			x += int(cmd[1])
			y += int(aim * int(cmd[1]))
		elif cmd[0] == "up":
			aim -= int(cmd[1])
		else:
			aim += int(cmd[1])

	print(x * y)

if __name__ == "__main__":
	with open("input_1.txt") as f:
		data = f.readlines()

	part_0(data)
	part_1(data)