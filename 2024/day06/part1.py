import numpy as np

# walking direction of guard
direction = np.array([-1,0])    # UP

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

# convert the map into an array
temp = []
for line in contents:
    temp.append(list(line.split()[0]))
array = np.asarray(temp)

# find the starting position of the guard
pos = np.argwhere(array=='^')[0]

# visited grid cells
total = 0

# patrol protocol
while True:
    # calculate next position
    step = pos+direction

    # check if out of bounds
    if step[0] < 0 or step[0] >= np.shape(array)[0] or step[1] < 0 or step[1] >= np.shape(array)[1]:
        if array[pos[0],pos[1]] != 'X':
            total += 1
        array[pos[0],pos[1]] = 'X'
        break

    if array[step[0],step[1]]=='#':
        direction = np.matmul(np.array([[0,1],[-1,0]]),direction)
    else:
        if array[pos[0],pos[1]] != 'X':
            total += 1
            array[pos[0],pos[1]] = 'X'
        pos += direction

print(total)