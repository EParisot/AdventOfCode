import sys

datas = [val.split("\n")[0] for val in sys.stdin]

positions = []
for data in datas:
    positions.append((int(data.split(", ")[0]), int(data.split(", ")[1])))
#print(positions, len(positions))

_max = 0
for val in positions:
    if max(val) > _max:
        _max = max(val)
#print(_max)

area = [['.'] * (_max + 1) for elem in range(_max + 1)]
letter = 65
for point in positions:
    area[point[1]][point[0]] = chr(letter)
    if letter <= 90 or letter <= 122:
        letter += 1
    elif letter > 90 and letter < 97:
        letter = 97
    elif letter > 122:
        letter = 65

def is_unique(val, tab):
    seen = set()
    uniq = True
    for elem in tab:
        if elem == val and elem not in seen:
            seen.add(elem)
        elif elem == val:
            uniq = False
    return uniq

for line in area:
    print(line)

def manhattan_distance(point, letter):
    return abs(point[0] - letter[0]) + abs(point[1] - letter[1])

def minkey(d):
     """ a) create a list of the dict's keys; 
         b) return the min key"""  
     k=list(d.keys())
     return min(k)

mem_dict = {}
for y, line in enumerate(area):
    for x, point in enumerate(line):
        tab = []
        for letter in positions:
            m_dist = manhattan_distance((x, y), \
                                        (letter[0], letter[1]))
            tab.append(m_dist)
        if sum(tab) < 10000: # or 10000
            mem_dict[sum(tab)] = (x, y)
            area[y][x] = '#'

print(mem_dict)

for line in area:
    print(line)

min_key = minkey(mem_dict)
print(min_key, mem_dict[min_key])

c = 0
for line in area:
    for char in line:
        if char == '#':
            c += 1

print(c)
