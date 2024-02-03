s = input()
l = ""
for i in range(0, len(s)):
    if i % 3 != 0:
        l += s[i]
print(l)