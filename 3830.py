_list = list(map(int, input().split()))
count = 0
for i in _list:
    if i > 0:
        count += 1
print(count)
