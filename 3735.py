s = input()
print(s[2])
print(s[-2])
print(s[0:5])
print(s[0:-2])
for i in range(0, len(s), 2):
    print(s[i], end="")
print()
for i in range(1, len(s), 2):
    print(s[i], end="")
print()
for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
print()
for i in range(len(s)-1, -1, -2):
    print(s[i], end="")
print()
print(len(s))