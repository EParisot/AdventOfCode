import sys

for val in sys.stdin:
    datas = val

print(datas)
datas = list(datas)

def is_finished(tab):
    ret = True
    i = 0
    while i < len(tab) - 1:
        if ord(tab[i]) == ord(tab[i + 1]) + 32 \
           or ord(tab[i]) == ord(tab[i + 1]) - 32:
            ret = False
        i += 1
    return ret

def reduce(datas):
    while is_finished(datas) == False:
        i = 0
        while i < len(datas) - 1:
            if ord(datas[i]) == ord(datas[i + 1]) + 32 \
               or ord(datas[i]) == ord(datas[i + 1]) - 32:
                datas.pop(i)
                datas.pop(i)
                i -= 1
                continue
            else:
                i += 1
        return len(datas)

# get uniques values
seen = set()
uniq_l = []
uniq_u = []
for elem in datas:
    if elem not in seen:
        seen.add(elem)
        if elem.islower():
            uniq_l.append(elem)
        else:
            uniq_u.append(elem)
uniq_l = sorted(uniq_l)
uniq_u = sorted(uniq_u)

# delete unique values and reduce
res_tab = []
for i, elem in enumerate(uniq_l):
    temp_data = [val for val in datas] 
    if ord(elem) == ord(uniq_u[i]) + 32 :
        j = 0
        while j < len(temp_data):
            if elem == temp_data[j]:
                temp_data.pop(j)
            elif uniq_u[i] == temp_data[j]:
                temp_data.pop(j)
            else:
                j += 1
        res_tab.append(reduce(temp_data))

print("\n", min(res_tab))

