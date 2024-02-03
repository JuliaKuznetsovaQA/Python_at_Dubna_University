_list = list(map(int, input().split()))
last = _list[-1]
for i in range((len(_list)-2), -1, -1):
    _list[i+1] = _list[i]
_list[0] = last
print(*_list)