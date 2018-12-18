import sys
import time


datas = [val for val in sys.stdin]

def parse(datas):
    res = []
    for data in datas:
        date = data[1:].split("]")[0]
        conv = time.strptime(date,"%Y-%m-%d %H:%M")
        date = time.strftime("%Y-%m-%d %H:%M", conv)
        if int(time.strftime("%H", conv)) == 23:
            _time = "00:00"
        else:
            _time = time.strftime("%H:%M", conv)
        if "#" in data:
            state = "#" + data.split("#")[1].split(" ")[0]
        else:
            if "wakes up" in data.split("] ")[1]:
                state = 1
            else:
                state = 0
        res.append([date, state, _time])
    return (res)

datas = parse(datas)
datas = sorted(datas, key=lambda datas: datas[0])

for data in datas:
    print(data)

turns = []
cur_tab = ["1"] * 60
old_id = datas[0][1]
datas.pop(0)
for i, data in enumerate(datas):
    if isinstance(data[1], str) and "#" in data[1]:
        new_id = data[1]
        turns.append({old_id: cur_tab})
        cur_tab = ["1"] * 60
        old_id = new_id
    if data[1] == 1 and datas[i - 1][1] == 0:
        start = time.strptime(datas[i - 1][2],"%H:%M")
        end = time.strptime(data[2],"%H:%M")
        chunk = int(time.strftime("%M", end)) - int(time.strftime("%M", start))
        cur_tab[int(time.strftime("%M", start)) : int(time.strftime("%M", end))] = ["0"] * chunk
    if i == len(datas) - 1:
        turns.append({old_id: cur_tab})

print("\nID  Minute\
        \n    000000000011111111112222222222333333333344444444445555555555\
        \n    012345678901234567890123456789012345678901234567890123456789\n")


for turn in turns:
    for key, val in turn.items():
        print(key, ''.join(val))

guards_s = {}
for turn in turns:
    for key, val in turn.items():
        if key not in guards_s:
            guards_s[key] = 60 - sum([int(i) for i in val])
        else:
            guards_s[key] += 60 - sum([int(i) for i in val])

print("\n", guards_s)

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

sleepy_guard = keywithmaxval(guards_s)
print("\n", sleepy_guard)

guards_sleep = [0] * 60
for turn in turns:
    for key, val in turn.items():
        if key == sleepy_guard:
            for i, elem in enumerate(guards_sleep):
                guards_sleep[i] += 0 if val[i] == "1" else 1

sleepy_minute = guards_sleep.index(max(guards_sleep))
print("\n", sleepy_minute)
sleepy_guard = int(keywithmaxval(guards_s)[1:])
print("\n", sleepy_minute * sleepy_guard)
