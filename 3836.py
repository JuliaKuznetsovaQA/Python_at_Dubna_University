_list = list(map(int, input().split()))
n = []
for i in range(0, len(_list)):
    if _list[i] % 2 == 1:
        n.append(_list[i])
if len(n) == 0:
    print(0)
else:
    _min = n[0]
    for i in range(1, len(n)):
        if n[i] < _min:
            _min = n[i]
    print(_min)