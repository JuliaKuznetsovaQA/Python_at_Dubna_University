num = int(input())
count = 0
while num != 0:
    num1 = int(input())
    if num1 > num:
        count += 1
    num = num1
print(count)