x, y = map(int, input().split())
z = 0
for i in range (0, abs(y)):
    z += abs(x)
if (x < 0 and y > 0) or (x > 0 and y < 0):
    print(0-z)
else:
    print(z)