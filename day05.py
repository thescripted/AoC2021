import re
from collections import defaultdict

with open('input.txt') as f:
    lines = [i.rstrip() for i in f.readlines()]

point = defaultdict(int)
for line in lines:
    x1, y1, x2, y2 = re.compile(r'\d+').findall(line)
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            point[(x1, i)] += 1
    elif y1 == y2:
        for j in range(min(x1, x2), max(x1, x2) + 1):
            point[(j, y1)] += 1
    else:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for k in range(x1, x2 + 1):
            if y2 > y1:
                point[(k, y1 + (k - x1))] += 1
            else:
                point[(k, y1 - (k - x1))] += 1
result = 0
for v in point.values():
    if v > 1:
        result += 1

print(result)
