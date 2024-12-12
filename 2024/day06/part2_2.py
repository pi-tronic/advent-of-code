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
start = np.argwhere(array=='^')[0]
pos = start.copy()

# visited grid cells
total = 0

potential_obstacles = []

# patrol protocol
while True:
    # calculate next position
    step = pos+direction

    # check if out of bounds
    if step[0] < 0 or step[0] >= np.shape(array)[0] or step[1] < 0 or step[1] >= np.shape(array)[1]:
        break

    if array[step[0],step[1]]=='#':
        direction = np.matmul(np.array([[0,1],[-1,0]]),direction)
    else:
        if [step[0],step[1]] not in potential_obstacles:
            potential_obstacles.append([step[0],step[1]])
        pos += direction

for point in potential_obstacles:
    temp = array[point[0],point[1]]
    if temp=='.':
        array[point[0],point[1]] = '#'
    else:
        continue

    pos = start.copy()
    # walking direction of guard
    direction = np.array([-1,0])    # UP

    path = [[pos[0], pos[1], direction[0], direction[1]]]

    # patrol protocol
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

    array[point[0],point[1]] = temp

    print(f"{potential_obstacles.index(point)}/{len(potential_obstacles)}   : {total}")

print(total)

# 1831