s = input()
l = ""
for i in range(len(s)-1, -1, -1):
    l += s[i]
if s == l:
    print('YES')
else:
    print('NO')