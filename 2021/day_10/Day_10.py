pairs = {
	'(': ')',
	'[': ']',
	'{': '}',
	'<': '>',
}

def recursive(line, i):
	if i == len(line):
		return i
	if line[i] in "([{<":
		track.append(line[i])
	else:
		if line[i] == pairs[track[-1]]:
			track.pop(-1)
		else:
			return i
	return recursive(line, i+1)

def part_0(data):
	scores = {"(": 3, "[": 57, "{": 1197, "<": 25137,
			")": 3, "]": 57, "}": 1197, ">": 25137	
	}
	score = 0
	for l in data:
		global track
		track = []
		res = recursive(l, 0)
		if res < len(l):
			score += scores[l[res]]
			#print(res, "/", len(l))
	print(score)

def part_1(data):
	scores = {")": 1, "]": 2, "}": 3, ">": 4,}
	total_scores = []
	for l in data:
		global track
		track = []
		res = recursive(l, 0)
		if res == len(l):
			score = 0
			close_pattern = []
			for i in range(len(track)):
				close_pattern.append(pairs[track[i]])
			close_pattern.reverse()
			for i in range(len(close_pattern)):
				score *= 5
				score += scores[close_pattern[i]]
			total_scores.append(score)
	total_scores.sort()
	print(total_scores[len(total_scores) // 2])

if __name__ == "__main__":
	data = open("input_10.txt").read().splitlines()

	part_0(data)
	part_1(data)