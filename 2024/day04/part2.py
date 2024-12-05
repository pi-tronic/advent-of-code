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
mul = re.compile(r'SAM')
# pattern
val = re.compile(r'MAS')

total = 0

# straight
# go through all lines
# straight_centers = []
# for line in array:
#     # find all instances
#     line = ''.join(line)
#     res = re.findall(mul, line)
#     res2 = re.findall(val, line)
#     iter = re.finditer(mul, line)
#     iter2 = re.finditer(val, line)
#     for foreward in range(len(res)):
#         straight_centers.append(min(next(iter).span()) + 1)
#     for backward in range(len(res2)):
#         straight_centers.append(min(next(iter2).span()) + 1)

# for line in array.T:
#     # find all instances
#     line = ''.join(line)
#     res = re.findall(mul, line)
#     res2 = re.findall(val, line)
#     iter = re.finditer(mul, line)
#     iter2 = re.finditer(val, line)
#     for foreward in range(len(res)):
#         if min(next(iter).span()) + 1 in straight_centers:
#             total += 1
#     for backward in range(len(res2)):
#         if min(next(iter2).span()) + 1 in straight_centers:
#             total += 1

diagonal_centers = []
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
    iter = re.finditer(mul, line)
    iter2 = re.finditer(val, line)
    for foreward in range(len(res)):
        t = min(next(iter).span()) + 1
        diagonal_centers.append([b+t, a+t])
    for backward in range(len(res2)):
        t = min(next(iter2).span()) + 1
        diagonal_centers.append([b+t, a+t])

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
    iter = re.finditer(mul, line)
    iter2 = re.finditer(val, line)
    for foreward in range(len(res)):
        t = min(next(iter).span()) + 1
        if [b+t, a-t] in diagonal_centers:
            total += 1
    for backward in range(len(res2)):
        t = min(next(iter2).span()) + 1
        if [b+t, a-t] in diagonal_centers:
            total += 1

print(total)