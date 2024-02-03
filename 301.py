a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - 4 * a * c
if d == 0:
    print(-b / (2 * a))
elif d < 0:
    print()
elif d > 0:
    print((-b + d ** 0.5) / (2 * a))
    print((-b - d ** 0.5) / (2 * a))