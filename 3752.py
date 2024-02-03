s = list(map(int, input().split()))
n = set()
for i in s:
    if i in n:
        print('YES')
    else:
        print('NO')
        n.add(i)

