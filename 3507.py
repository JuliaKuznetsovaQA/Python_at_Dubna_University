a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
elif a != b and b != c and a != c:
    print(0)