s = input()
p = ".,;:!?"
count = 0
for i in s:
    if i in p:
        count += 1
print(count)