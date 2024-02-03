n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

max_ = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > max_:
            max_ = a[i][j]
            index_n = i
            index_m = j
if max_ == 0:
    index_n = 0
    index_m = 0
print(max_)
print(index_n, index_m)