def part_0(data):
	res = 0
	for r in data:
		row_data = r.split("|")[1].split()
		for num in row_data:
			if len(str(num)) == 2 or len(str(num)) == 4 or len(str(num)) == 3 or len(str(num)) == 7:
				res += 1
	print(res)

def guess_numbers(corresp, output_data):
	res = []
	for num in output_data:
		if len(str(num)) == 2:
			res.append(1)
		elif len(str(num)) == 3:
			res.append(7)
		elif len(str(num)) == 4:
			res.append(4)
		elif len(str(num)) == 7:
			res.append(8)
		elif sum([corresp["r1_r2"][0] in num, corresp["r1_r2"][1] in num]) == 1 and \
				sum([corresp["l1_mid"][0] in num, corresp["l1_mid"][1] in num]) == 1 and \
				sum([corresp["l2_bot"][0] in num, corresp["l2_bot"][1] in num]) == 2 and \
				corresp["top"] in num:
			res.append(2)
		elif sum([corresp["r1_r2"][0] in num, corresp["r1_r2"][1] in num]) == 2 and \
				sum([corresp["l1_mid"][0] in num, corresp["l1_mid"][1] in num]) == 1 and \
				sum([corresp["l2_bot"][0] in num, corresp["l2_bot"][1] in num]) == 1 and \
				corresp["top"] in num:
			res.append(3)
		elif sum([corresp["r1_r2"][0] in num, corresp["r1_r2"][1] in num]) == 1 and \
				sum([corresp["l1_mid"][0] in num, corresp["l1_mid"][1] in num]) == 2 and \
				sum([corresp["l2_bot"][0] in num, corresp["l2_bot"][1] in num]) == 1 and \
				corresp["top"] in num:
			res.append(5)
		elif sum([corresp["r1_r2"][0] in num, corresp["r1_r2"][1] in num]) == 1 and \
				sum([corresp["l1_mid"][0] in num, corresp["l1_mid"][1] in num]) == 2 and \
				sum([corresp["l2_bot"][0] in num, corresp["l2_bot"][1] in num]) == 2 and \
				corresp["top"] in num:
			res.append(6)
		elif sum([corresp["r1_r2"][0] in num, corresp["r1_r2"][1] in num]) == 2 and \
				sum([corresp["l1_mid"][0] in num, corresp["l1_mid"][1] in num]) == 2 and \
				sum([corresp["l2_bot"][0] in num, corresp["l2_bot"][1] in num]) == 1 and \
				corresp["top"] in num:
			res.append(9)
		elif sum([corresp["r1_r2"][0] in num, corresp["r1_r2"][1] in num]) == 2 and \
				sum([corresp["l1_mid"][0] in num, corresp["l1_mid"][1] in num]) == 1 and \
				sum([corresp["l2_bot"][0] in num, corresp["l2_bot"][1] in num]) == 2 and \
				corresp["top"] in num:
			res.append(0)
	return res

def part_1(data):
	res = 0
	for r in data:
		input_data = r.split("|")[0].split()
		output_data = r.split("|")[1].split()
		corresp = {"r1_r2": [], "top": "", "l1_mid": [], "l2_bot": []}
		for num in input_data:
			# 2 right segments
			if len(str(num)) == 2:
				corresp["r1_r2"] = [num[0], num[1]]
		for num in input_data:
			# top segment
			if len(str(num)) == 3:
				for c in num:
					if not c in corresp["r1_r2"]:
						corresp["top"] = c
						break
		for num in input_data:
			# top left and mid segments
			if len(str(num)) == 4:
				for c in num:
					if not c in corresp["l1_mid"] and not c in corresp["r1_r2"]:
						corresp["l1_mid"].append(c)
		for num in input_data:
			# bottom left and bottom segments
			if len(str(num)) == 7:
				for c in num:
					if not c in corresp["l2_bot"] and not c in corresp["r1_r2"] and not c in corresp["l1_mid"] and c != corresp["top"]:
						corresp["l2_bot"].append(c)
		res += int("".join(list(map(str, guess_numbers(corresp, output_data)))))
	print(res)

if __name__ == "__main__":
	data = open("input_8.txt").read().splitlines()

	part_0(data)
	part_1(data)