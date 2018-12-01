import sys

res = 0
res_tab = [0]

datas = [int(val) for val in sys.stdin]

#find first redondant result

while True:
    for line in datas:
        res += line
        if res in res_tab:
            print(res)
            exit(0)
        res_tab.append(res)
