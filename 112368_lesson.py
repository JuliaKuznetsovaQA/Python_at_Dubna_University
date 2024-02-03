N, M = map(int, input().split())
list_b = []
for i in range(N):
    a = list(map(int, input().split()))
    list_b.append(a)

_max = list_b[0][0]
for a in list_b:
    a_max = max(a)
    if a_max > _max:
        _max = a_max

j_max = 0
for i in range(N):
    for j in range(M):
        if list_b[i][j] == _max:
            j_max = j
            print()
            for k in range(N):
                print(list_b[k][j_max], end=" ")
            break

