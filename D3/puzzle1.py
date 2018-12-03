import sys

datas = [val for val in sys.stdin]

def parse(datas):
    res = []
    for data in datas:
        x = int(data.split("@")[1].split(",")[0])
        y = int(data.split(",")[1].split(":")[0])
        w = int(data.split(":")[1].split("x")[0])
        h = int(data.split("x")[1])
        res.append([x, y, w, h])
    return (res) 

datas = parse(datas)       

n = 1024
m = 1024
area = [[0] * m for i in range(n)]
res = 0

for data in datas:
    for h in range(data[3]):
        for w in range(data[2]):
            if area[data[0] + w][data[1] + h] == 0:
                area[data[0] + w][data[1] + h] = 1
            elif area[data[0] + w][data[1] + h] == 1:
                res += 1
                area[data[0] + w][data[1] + h] += 1
            else:
                area[data[0] + w][data[1] + h] += 1

for data in datas:
    is_the_one = True
    for h in range(data[3]):
        for w in range(data[2]):
            if area[data[0] + w][data[1] + h] != 1:
                is_the_one = False
                break
        if is_the_one == False:
            break
    else:
        if is_the_one == True:
            print(datas.index(data) + 1)
            
