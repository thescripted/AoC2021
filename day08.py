with open('input.txt') as f:
    lines = [[j.strip() for j in i.rstrip().split('|')] for i in f.readlines()]

# Part 1
segment_set = set([2, 3, 4, 7])
count = 0
for line in lines:
    for segment in line[1].split(' '):
        count += 1 if len(segment) in segment_set else 0
print(count)


def segment_decoder(line):
    numbers = line.split(' ')
    resolved_segments = ['' for _ in range(7)]
    one = set([i for i in numbers if len(i) == 2][0])
    seven = set([i for i in numbers if len(i) == 3][0])
    four = set([i for i in numbers if len(i) == 4][0])
    eight = set([i for i in numbers if len(i) == 7][0])
    three = set([i for i in numbers if len(i) == 5 and len(set(i) - seven) == 2][0])
    nine = three | four
    five = set([i for i in numbers if len(i) == 5 and len(nine - set(i)) == 1 and set(i) != three][0])

    resolved_segments[0] = (seven - one).pop()
    resolved_segments[1] = (four - three).pop()
    resolved_segments[2] = (four - five).pop()
    resolved_segments[4] = (eight - three - four).pop()
    resolved_segments[5] = (seven - set(resolved_segments[0] + resolved_segments[2])).pop()
    resolved_segments[6] = (eight - four - seven - set(resolved_segments[4])).pop()
    resolved_segments[3] = (set('abcdefg') - set([i for i in resolved_segments if i != ''])).pop()

    return resolved_segments


total = 0
for line in lines:
    segments, output = line[0], line[1]
    decoder = segment_decoder(segments)
    result = 0
    print(output)
    numbers = output.split(' ')
    for number in numbers:
        for value in number:
            num = decoder.index(value) + 1
            result = result*10 + num
    total += result
    exit(0)
print(total)
