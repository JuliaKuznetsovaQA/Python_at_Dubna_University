n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))


summa = 0
for i in range(n):
    for j in range(m):
        summa += a[i][j]

print(summa)