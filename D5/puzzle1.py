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
            
print("\n", reduce(datas))
