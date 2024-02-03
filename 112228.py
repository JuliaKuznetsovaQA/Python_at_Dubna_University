import math

def is_simple(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        else:
            i = i + 1
    return True

a, b = map(int, input().split())
l = 0
for i in range(a, b+1):
    if is_simple(i):
        print(i, end=" ")
        l += 1
if l == 0:
    print(l)

