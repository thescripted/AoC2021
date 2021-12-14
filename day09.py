from collections import deque
import heapq

with open('input.txt') as f:
    heatmap = [list(map(int, list(line.rstrip()))) for line in f.readlines()]

risk_level = 0
row = len(heatmap)
col = len(heatmap[0])

# Part 1
for i in range(row):
    for j in range(col):
        point = heatmap[i][j]
        if i > 0 and point >= heatmap[i-1][j]:
            continue
        if j < (col - 1) and point >= heatmap[i][j+1]:
            continue
        if i < (row - 1) and point >= heatmap[i+1][j]:
            continue
        if j > 0 and point >= heatmap[i][j-1]:
            continue
        risk_level += point + 1


def get_basin_size(heatmap, row, col):
    visited = set()
    queue = deque([(row, col)])
    r = len(heatmap)
    c = len(heatmap[0])

    basin_size = 0
    while queue:
        i, j = queue.popleft()
        if (i, j) in visited:
            continue

        visited.add((i, j))
        basin_size += 1
        if i > 0 and heatmap[i-1][j] != 9:
            queue.append((i-1, j))
        if j > 0 and heatmap[i][j-1] != 9:
            queue.append((i, j-1))
        if i < (r - 1) and heatmap[i+1][j] != 9:
            queue.append((i+1, j))
        if j < (c - 1) and heatmap[i][j+1] != 9:
            queue.append((i, j+1))
    return basin_size


# Part 2
heap = []
capacity = 3
for i in range(row):
    for j in range(col):
        point = heatmap[i][j]
        if i > 0 and point >= heatmap[i-1][j]:
            continue
        if j < (col - 1) and point >= heatmap[i][j+1]:
            continue
        if i < (row - 1) and point >= heatmap[i+1][j]:
            continue
        if j > 0 and point >= heatmap[i][j-1]:
            continue
        size = get_basin_size(heatmap, i, j)
        if len(heap) < capacity:
            heapq.heappush(heap, size)
        else:
            if size > heap[0]:
                heapq.heappushpop(heap, size)
print(heap[0]*heap[1]*heap[2])
