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

def manhattan_distance(point, letter):
    return abs(point[0] - letter[0]) + abs(point[1] - letter[1])

for y, line in enumerate(area):
    for x, point in enumerate(line):
        if point == '.':
            tab = []
            for letter in positions:
                m_dist = manhattan_distance((x, y), \
                                            (letter[0], letter[1]))
                tab.append(m_dist)
            min_dist = min(tab)
            if is_unique(min_dist, tab):
                area[y][x] = chr(97 + tab.index(min_dist))

for line in area:
    print(line)

count_dict = {}
for line in area:
    for char in line:
        if char != '.':
            char = chr(ord(char) + 32 if char.isupper() else ord(char) + 0)
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1

for elem in area[0]:
    if elem in count_dict:
        del count_dict[elem]
    
for elem in area[-1]:
    if elem in count_dict:
        del count_dict[elem]
    
for line in area:
    if line[0] in count_dict:
        del count_dict[line[0]]

for line in area:
    if line[-1] in count_dict:
        del count_dict[line[-1]]
    
print("\n", count_dict)

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

print(keywithmaxval(count_dict))
