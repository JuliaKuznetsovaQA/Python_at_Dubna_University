_list = list(map(int, input().split()))
max_count = 1
l = _list[0]
for i in range(0, len(_list)):
    count = 1
    for j in range((i + 1), len(_list)):
        if _list[j] == _list[i]:
            count += 1
    if count > max_count:
        max_count = count
        l = _list[i]
print(l)