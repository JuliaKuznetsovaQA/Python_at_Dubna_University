n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    n_min = a[i][0]
    for j in range(m):
        index = 0
        if a[i][j] < n_min:
            n_min = a[i][j]
            index = j
        for i in range(n):
            if a[i][index] > n_min:
                break
            else:
                print(i, index)



