from collections import deque

with open('input.txt') as f:
    fishes = [int(i) for i in f.readline().split(',')]

# Part 1
for _ in range(80):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes.append(8)
            fishes[i] = 6
        else:
            fishes[i] -= 1
print(len(fishes))

# Part 2
with open('input.txt') as f:
    fishes = [int(i) for i in f.readline().split(',')]


def get_fishes(day, fish, mapper):
    total_days = 256
    if (day, fish) in mapper:
        return mapper[(day, fish)]

    total_babies = 1
    for i in range(day + fish + 1, total_days + 1, 7):
        total_babies += get_fishes(i, 8, mapper)
    mapper[(day, fish)] = total_babies
    return total_babies


mapper = {}
total_fishes = 0
for fish in fishes:
    total_fishes += get_fishes(0, fish, mapper)

print(total_fishes)

# Part 2 (w/o Recursion)

with open('input.txt') as f:
    fishes = [int(i) for i in f.readline().split(',')]

fishpool = deque([0 for _ in range(9)])
for fish in fishes:
    fishpool[fish] += 1

for _ in range(256):
    fishpool.rotate(-1)
    fishpool[6] += fishpool[8]

print(sum(fishpool))
