s = input()
n = input()
count = 0
for i in range(0, len(s)):
    l = i + len(n)
    if s[i:l] == n:
        count += 1
print(count)
