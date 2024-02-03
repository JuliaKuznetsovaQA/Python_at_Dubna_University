import math


def is_simple(num):
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        else:
            i = i + 1
    return True


num = int(input())
if is_simple(num):
    print("Yes")
else:
    print("No")

def is_prime(number):
    for d in range(2, number//2+1):
        if number % d == 0:
            return False
    return True

a, b = map(int, input().split())
f = True
for i in range(a, b+1):
    if is_prime(i):
        print(i, end=' ')
        f = False
if f:
    print(0)


def sieve_eratosthenes(b):
    _list = [i for i in range(0, b+1)]
    for i in range(2, b+1):
        if _list[i] != 0:
            for j in range(i*i, len(_list), i):
                _list[j] = 0
    return _list