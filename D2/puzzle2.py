import sys

datas = [val for val in sys.stdin]

for cur_elem in datas:
    for elem in datas:
        diff = 0
        pos = 0
        for i, char in enumerate(elem):
            if char != cur_elem[i]:
                diff += 1
                pos = i
            if diff > 1:
                break
        if diff == 1:
            print(datas.index(cur_elem), cur_elem)
            print(datas.index(elem), elem)
            print("result = "+ cur_elem[:pos] + cur_elem[pos+1:])
            exit(0)
