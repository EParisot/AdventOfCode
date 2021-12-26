import sys

datas = [val for val in sys.stdin]

res_tab = [0, 0]

for elem in datas:
    x2 = 0
    x3 = 0
    for cur_char in elem:
        i = 0
        for char in elem:
            if cur_char == char:
                i += 1
        if i == 2:
            x2 = 1
        elif i == 3:
            x3 = 1
    res_tab[0] += x2
    res_tab[1] += x3
    print(elem, x2, x3)

print("result = " + str(res_tab[0] * res_tab[1]))
