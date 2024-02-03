n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

sum_min = sum(a[0])
summa = 0
index = 0
for i in range(n):
    for j in range(m):
        summa += a[i][j]
    if sum_min > summa:
        sum_min = summa
        index = i
    summa = 0
print(*a[index])