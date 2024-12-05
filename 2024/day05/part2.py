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

rules = np.take(rules, np.argsort(rules[:,0], axis=0), axis=0)

total = 0
for line in range(len(contents)):
    correct = True
    while True:
        fixed = True
        for item in range(len(contents[line])):
            for rule in np.argwhere(rules[:,0]==contents[line][item]):
                if rules[rule[0],1] in contents[line]:
                    # find indices and check order
                    ind = contents[line].index(rules[rule[0],1])
                    if item > ind:
                        correct = False
                        fixed = False
                        temp = contents[line][item]
                        contents[line][item] = contents[line][ind]
                        contents[line][ind] = temp
        if correct or fixed:
            break

    if not correct:
        total += int(contents[line][int(len(contents[line])/2)])


# find all
# indices = [i for i, x in enumerate(my_list) if x == "whatever"]
# np.argwhere(array==number)

print(total)