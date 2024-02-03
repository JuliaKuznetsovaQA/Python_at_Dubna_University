n = int(input())
a = b = 1
if n == 0:
    print()
elif n == 1:
    print(1)
elif n == 2:
    print("1 1")
else:
    print("1 1", end=" ")
    for i in range (2, n):
        print(a + b, end= " ")
        c = a
        a = b
        b = c + b
