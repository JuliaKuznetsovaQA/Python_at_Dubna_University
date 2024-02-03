_list = list(map(int, input().split()))
m = _list[0]
n = 0
for i in range(1, len(_list)):
    if _list[i] > m:
        m = _list[i]
        n = i
print(m, n)