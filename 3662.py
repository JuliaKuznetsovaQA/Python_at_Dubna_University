a = int(input())
if a == 0:
    max_count = 0
else:
    b = int(input())
    count = 1
    max_count = 1
    while b != 0:
        if a == b:
            count += 1
            if count > max_count:
                max_count = count
        elif a != b:
            count = 1
        a = b
        b = int(input())
    if count > max_count:
        max_count = count
print(max_count)