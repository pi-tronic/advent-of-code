import itertools

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

total = 0

for line in contents:
    # print(line[:-1])
    wanted = int(line.split(':')[0])
    values = line[:-1].split(':')[1][1:].split(' ')
    # print(wanted, values)

    combs = list(map(list, itertools.product(['+', '*', '||'], repeat=len(values)-1)))
    for comb in combs:
        v = iter(values)
        res = int(next(v))
        for operation in comb:
            if operation=='+':
                res += int(next(v))
            if operation=='*':
                res *= int(next(v))
            if operation=='||':
                next_v = next(v)
                res *= 10**len(next_v)
                res += int(next_v)
        if res==wanted:
            total += res
            break

print(total)