import numpy as np

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
start = np.argwhere(array=='^')[0]

# loops
total = 0

for y in range(np.shape(array)[0]):
    for x in range(np.shape(array)[1]):
        temp = array[y,x]
        if temp=='.':
            array[y,x] = '#'
        else:
            continue

        pos = start.copy()
        # walking direction of guard
        direction = np.array([-1,0])    # UP

        path = [[pos[0], pos[1], direction[0], direction[1]]]

        # patrol protocol
        max_i = 5000
        while True:
            # calculate next position
            step = pos+direction

            # check if out of bounds
            if step[0] < 0 or step[0] >= np.shape(array)[0] or step[1] < 0 or step[1] >= np.shape(array)[1]:
                break

            if array[step[0],step[1]]=='#':
                direction = np.matmul(np.array([[0,1],[-1,0]]),direction)
            else:
                pos += direction

            if [pos[0], pos[1], direction[0], direction[1]] in path:
                total += 1
                break
            else:
                path.append([pos[0], pos[1], direction[0], direction[1]])

        array[y,x] = temp

        print(y, x)

print(total)