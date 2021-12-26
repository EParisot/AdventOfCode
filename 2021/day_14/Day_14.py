def part_0(template, pairs):
	for r in range(10):
		replaced = []
		for i in range(len(template)):
			if i < len(template) - 1 and template[i:i+2] in pairs:
				replaced.append(pairs[template[i:i+2]][:-1] if i < len(template) - 2 else pairs[template[i:i+2]])
		template = ''.join(replaced)
		
	counts = {k: template.count(k) for k in template}
	print(counts[max(counts, key=lambda x: counts[x])] - counts[min(counts, key=lambda x: counts[x])])

def part_1(template, pairs):
	double_counts = {k: 0 for k, v in pairs.items()}
	for i in range(len(template)-1):
		double_counts[template[i:i+2]] += 1
	for r in range(40):
		to_add = {k:0 for k, v in double_counts.items()}
		for double in double_counts:
			if double_counts[double]:
				to_add[double[0] + pairs[double][1]] += double_counts[double]
				to_add[pairs[double][1] + double[1]] += double_counts[double]
				double_counts[double] = 0
		for d in to_add:
			double_counts[d] += to_add[d]
	letter_counts = {}
	for pair, count in double_counts.items():
		letter_counts[pair[0]] = 0
		letter_counts[pair[1]] = 0
	for pair, count in double_counts.items():
		letter_counts[pair[0]] += count // 2
		letter_counts[pair[1]] += count // 2

	print(letter_counts[max(letter_counts, key=lambda x: letter_counts[x])] - letter_counts[min(letter_counts, key=lambda x: letter_counts[x])])

if __name__ == "__main__":
	data = open("input_14.txt").read().splitlines()

	template = data[0]
	pairs = data[2:]
	pairs_dict = {}
	for i, p in enumerate(pairs):
		pair = p.split(" -> ")
		pairs_dict[pair[0]] = pair[1]
	
	for p, v in pairs_dict.items():
		pairs_dict[p] = p[0] + v + p[1]

	part_0(template, pairs_dict)
	part_1(template, pairs_dict)