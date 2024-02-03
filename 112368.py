n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input().split())
a = [[int(j) for j in i] for i in a]

k = max(a[0])
for i in range(n):
    if max(a[i]) > k:
        k = max(a[i])

for i in range(m):
    for j in range(n):
        if a[j][i] == k:
            print(*[a[l][i] for l in range(n)])
            break