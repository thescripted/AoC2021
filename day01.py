with open('01_input.txt') as f:
    content = [int(i.rstrip()) for i in f.readlines()]

# Part 1
count = 0
for i in range(1, len(content)):
    if content[i] > content[i-1]:
        count += 1
print(count)

# Part 2
count = 0
for i in range(1, len(content) - 2):
    if sum(content[i:i+3]) > sum(content[i-1:i+2]):
        count += 1
print(count)
