def get_data(root_content, check):
    content = root_content  # Copy content
    n = len(content)
    for i in range(n):
        common = 0
        for line in content:
            if line[i] == '1':
                common += 1
            else:
                common -= 1
        if common >= 0:
            content = [v for v in content if v[i] == ('0' if check else '1')]
        else:
            content = [v for v in content if v[i] == ('1' if check else '0')]
        if len(content) == 1:
            data = int(content[0], 2)
            break
    return data


with open('input.txt') as f:
    content = [i.rstrip() for i in f.readlines()]

# Part 1
alpha = 0
gamma = 0
n = len(content[0])
arr = [0 for _ in range(n)]
for line in content:
    for i in range(n):
        if line[i] == '1':
            arr[i] += 1
        else:
            arr[i] -= 1
for a in arr:
    if a > 0:
        alpha += 1
    else:
        gamma += 1
    alpha <<= 1
    gamma <<= 1
alpha >>= 1
gamma >>= 1
print(alpha*gamma)

# Part 2
ogr = get_data(content, True)
csr = get_data(content, False)

print(ogr*csr)
