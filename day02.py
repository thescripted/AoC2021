with open('input.txt') as f:
    content = [i.rstrip() for i in f.readlines()]

# Part 1
forward = 0
depth = 0
for line in content:
    direction, value = line.split(' ')
    value = int(value)
    if direction == 'forward':
        forward += value
    elif direction == 'down':
        depth += value
    elif direction == 'up':
        depth -= value

print(depth*forward)

# Part 2
aim = 0
forward = 0
depth = 0
for line in content:
    direction, value = line.split(' ')
    value = int(value)
    if direction == 'forward':
        forward += value
        depth += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
print(depth*forward)
