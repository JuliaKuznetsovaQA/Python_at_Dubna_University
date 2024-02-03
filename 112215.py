n = int(input())
a = n % 10
while n > 10:
    if a != (n // 10) % 10:
        print("NO")
        break
    else:
        n = n // 10
if a == n:
    print("YES")