import numpy as np

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

array = np.zeros((len(contents), len(contents[0])-1))

for line in range(len(contents)):
    for col in range(len(contents[0])-1):
        if contents[line][col]=='.':
            array[line, col] = -1
        else:
            array[line, col] = int(contents[line][col])

starting_points = np.argwhere(array==0)

total = 0

def path(height, pos_pre, pos):
    global total
    dirs = [[1,0], [0,1], [-1,0], [0,-1]]
    for d in dirs:
        new_pos = [pos[0] + d[0], pos[1] + d[1]]
        if new_pos[0] >= 0 and new_pos[0] < len(contents) and new_pos[1] >= 0 and new_pos[1] < len(contents[0])-1:
            if array[new_pos[0],new_pos[1]]==height+1:
                if array[new_pos[0],new_pos[1]]==9:
                    total += 1
                else:
                    path(height+1, pos, new_pos)

for point in starting_points:
    total_now = total
    path(0, list(point), list(point))

print(total)
