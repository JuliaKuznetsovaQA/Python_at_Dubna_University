a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a >= b:
    if b >= c:
        n_max = a
        n_min = c
    else:   # c > b
        n_min = b
        if a >= c:
            n_max = a
        else:
            n_max = c
else:  # b > a
    if b >= c:
        n_max = b
        if c <= a:
            n_min = c
        else:
            n_min = a
    else:  # c > b
        n_max = c
        n_min = a
print(n_min)
print(n_max)


