with open('input.txt') as f:
    content = [int(i) for i in f.readline().split(',')]

fuel = None
mem = {}
for i in range(max(content) + 100):
    pivot = i
    current = 0
    for j in range(len(content)):
        diff = 0
        n = abs(i - content[j])
        if n in mem:
            diff = mem[n]
        else:
            for k in range(n):  # counter
                diff += k + 1
            mem[n] = diff
        current += diff
    print(current)
    fuel = current if fuel is None else min(current, fuel)

print("Min:", fuel)
