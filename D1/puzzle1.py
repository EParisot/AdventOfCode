import sys

res = 0
res_tab = [0]

datas = [int(val) for val in sys.stdin]

#find input sum

for line in datas:
    res += line

print(res)
