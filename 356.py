n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

summa = 0
sum_max = 0
for i in range(n):
    for j in range(m):
        summa += a[i][j]
    if summa > sum_max:
        sum_max = summa
        index = i
    summa = 0
print(sum_max)
print(index)