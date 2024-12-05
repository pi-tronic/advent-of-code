import numpy as np

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

for line in range(len(contents)):
    if contents[line] == '\n':
        rules = np.asarray(contents[:line])
        contents = contents[line+1:]
        break
    contents[line] = list(contents[line][:-1].split('|'))
for line in range(len(contents)):
    contents[line] = list(contents[line][:-1].split(','))

total = 0

for line in contents:
    correct = True
    for rule in rules:
        if rule[0] in line and rule[1] in line:
            # find indices and check order
            ind0 = line.index(rule[0])
            ind1 = line.index(rule[1])
            if ind0 > ind1:
                correct = False
                break
    if correct:
        total += int(line[int(len(line)/2)])


# find all
# indices = [i for i, x in enumerate(my_list) if x == "whatever"]
# np.argwhere(array==number)

print(total)