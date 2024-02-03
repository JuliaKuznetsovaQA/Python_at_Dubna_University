a, b = map(int, input().split())
count = 0
while min(a, b) != 0:
    m = max(a, b)
    n = min(a, b)
    a = m - n
    b = n
    count += 1
print(max(a, b), count)