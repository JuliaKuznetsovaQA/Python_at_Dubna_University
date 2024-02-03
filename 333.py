num = int(input())
_max = num
while num != 0:
    num = int(input())
    if num > _max:
        _max = num
print(_max)