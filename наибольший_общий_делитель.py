m = 15
n = 60
i = min(n, m)
d = 1
while i >= 1:
    if m % i == 0 and n % i == 0:
        d = i
        break
    i -= 1
print(d)