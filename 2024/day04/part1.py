import numpy as np
import re

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

for line in range(len(contents)):
    contents[line] = list(contents[line])[:-1]
array = np.asarray(contents)

# pattern
mul = re.compile(r'SAMX')
# pattern
val = re.compile(r'XMAS')

total = 0

# go through all lines
for line in array:
    # find all instances
    line = ''.join(line)
    res = re.findall(mul, line)
    res2 = re.findall(val, line)
    total += len(res) + len(res2)

for line in array.T:
    # find all instances
    line = ''.join(line)
    res = re.findall(mul, line)
    res2 = re.findall(val, line)
    total += len(res) + len(res2)

# top left down right
for i in range(sum(np.shape(array))-1):
    line = ''
    a = np.clip(i, 0, np.shape(array)[1]-1)
    b = np.clip(i-a, 0, np.shape(array)[0]-1)
    a = np.shape(array)[1] - 1 - a

    if a:
        lenght = np.shape(array)[1] - a
    elif b:
        lenght = np.shape(array)[0] - b
    else:
        lenght = min(np.shape(array))

    for t in range(lenght):
        line += array[b+t, a+t]
    
    res = re.findall(mul, line)
    res2 = re.findall(val, line)
    total += len(res) + len(res2)

# down left top right
for i in range(sum(np.shape(array))-1):
    line = ''
    a = np.clip(i, 0, np.shape(array)[1]-1)
    b = np.clip(i-a, 0, np.shape(array)[0]-1)
    a_temp = np.shape(array)[1] - 1 - a

    if a_temp:
        lenght = np.shape(array)[1] - a_temp
    elif b:
        lenght = np.shape(array)[0] - b
    else:
        lenght = min(np.shape(array))
    
    for t in range(lenght):
        line += array[b+t, a-t]

    res = re.findall(mul, line)
    res2 = re.findall(val, line)
    total += len(res) + len(res2)

print(total)