from random import randint

a = [0] * 6
for i in range(len(a)):
    a[i] = randint(-9, 10)
    print(a)

for i in a:
    if i < 0:
        counter += 1
        print(i, end="")