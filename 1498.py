x, y = input().split()
x = int(x)
y = int(y)
if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x == 0 or y == 0:
    print("Точка лежит на оси")