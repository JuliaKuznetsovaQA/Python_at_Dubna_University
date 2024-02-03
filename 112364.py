n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())

count = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == k:
            count += 1
print(count)