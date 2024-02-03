n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

saddle_points = []

for r, line in enumerate(matrix):
    minimum = min(line)
    for c, element in enumerate(line):
        if element == minimum == max([line[c] for line in matrix]):
            saddle_points.append([r + 1, c + 1])

for saddle_point in saddle_points:
    print(*saddle_point)
if len(saddle_points) == 0:
    print(0)