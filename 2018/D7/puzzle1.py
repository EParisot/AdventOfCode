import sys

datas = [val.split("\n")[0] for val in sys.stdin]

orders = []
for data in datas:
    order = []
    for word in data.split(' '):
        if len(word) == 1:
            order.append(word)
    orders.append(order)

orders_start = [order[0] for order in orders]
orders_end = [order[1] for order in orders]

conditions = {}
for end in orders_end:
    conditions[end] = []
    for i, data in enumerate(orders_end):
        if data == end and orders_start[i] not in conditions[end]:
            conditions[end].append(orders_start[i])
    conditions[end] = sorted(conditions[end])

print("Conditions :\n")
for key, val in conditions.items():
    print(key, val)

print("\nResult :\n")

def find_first(orders):
    for order in orders:
        if order[0] not in orders_end:
            return order[0]

def find_last(orders):
    for order in orders:
        if order[1] not in orders_start:
            return order

def do_step(start, orders, conditions, stucked, res):
    # handle first round
    if start == 0:
        start = find_first(orders)
        
    # Scan choices
    choices = []
    for order in orders:
        if order[0] == start:
            choices.append(order[1])
    choices = sorted(choices)
    choice = None
    
    # clean conditions
    for key, val in conditions.items():
        if start in val:
            conditions[key].remove(start)
    
    # if START_COND
    if start in conditions and len(conditions[start]) > 0:
        choice = conditions[start][0]
        stucked.append(start)
        print(start, conditions[start], choice, "START_COND")
        return do_step(choice, orders, conditions, stucked, res)

    # if NO_COND
    if start not in conditions or len(conditions[start]) == 0:
        res.append(start)
        # check end
        if start == find_last(orders)[1]:
            print("END")
            return res
        else:
            if len(stucked) > 0 and stucked[-1] in choices:
                choice = stucked[-1]
                stucked.pop(-1)
            else:
                choice = choices[0]
            print(start, choice, "NO_COND")
            return do_step(choice, orders, conditions, stucked, res)
        
print("\nFinal Order = ", ''.join(do_step(0, orders, conditions, [], [])))
