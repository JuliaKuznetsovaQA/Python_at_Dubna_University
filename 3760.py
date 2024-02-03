n = int(input())
d = dict()
for i in range(n):
    a, b = input().split()
    d[a] = b
    d[b] = a
word = input()
print(d[word])
