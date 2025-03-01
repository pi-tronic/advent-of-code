import numpy as np
from solve_graph import solve_graph

# get data
inputs = open('./demo_inputs2.txt')

# read in instruction lines
contents = inputs.readlines()

# array representation
array = np.asarray([np.array(list(line[:-1])) for line in contents])

# start + end position
start_position = np.argwhere(array=='S')[0]
end_position = np.argwhere(array=='E')[0]

# change start and and to free space
array[start_position[0], start_position[1]] = '.'
array[end_position[0], end_position[1]] = '.'

# find corners
corners = []
for row in range(np.shape(array)[0]):
    for col in range(np.shape(array)[1]):
        if array[row, col] == '.':
            # check if corner
            up_down = False
            left_right = False
            # up
            if row-1 >= 0:
                if array[row-1, col]=='.':
                    up_down = True
            # down
            if row+1 < np.shape(array)[0]:
                if array[row+1, col]=='.':
                    up_down = True
            # left
            if col-1 >= 0:
                if array[row, col-1]=='.':
                    left_right = True
            # right
            if col+1 < np.shape(array)[1]:
                if array[row, col+1]=='.':
                    left_right = True
            
            if up_down and left_right:
                corners.append([row, col])
if not np.any(np.all(start_position == corners, axis=1)):
    corners.append([start_position[0], start_position[1]])
if not np.any(np.all(end_position == corners, axis=1)):
    corners.append([end_position[0], end_position[1]])

edges = []
orientation = []
lenghts = []
test = np.asarray(corners)
rows = np.unique(test[:,1])
cols = np.unique(test[:,0])
for row in rows:
    cs = test[test[:,0]==row]
    for c in range(len(cs)-1):
        is_conescutive = True
        for v in range(cs[c,1]+1, cs[c+1,1]):
            if array[row, v] == '#':
                is_conescutive = False
                break
        if is_conescutive:
            index_0 = corners.index(list(cs[c]))
            index_1 = corners.index(list(cs[c+1]))
            edges.append([index_0,index_1])
            orientation.append('h')
            lenghts.append(cs[c+1,1]-cs[c,1])
for col in cols:
    cs = test[test[:,1]==col]
    for c in range(len(cs)-1):
        is_conescutive = True
        for v in range(cs[c,0]+1, cs[c+1,0]):
            if array[v, col] == '#':
                is_conescutive = False
                break
        if is_conescutive:
            index_0 = corners.index(list(cs[c]))
            index_1 = corners.index(list(cs[c+1]))
            edges.append([index_0,index_1])
            orientation.append('v')
            lenghts.append(abs(cs[c+1,0]-cs[c,0]))
edges.remove([34,35])
nodes = [i for i in range(len(corners))]
start = corners.index(list(start_position))
end = corners.index(list(end_position))

print(edges)
print(lenghts)
print(orientation)
print(corners)
print(start)
print(end)
print('\n')

paths = solve_graph(start, end, nodes, edges, lenghts, orientation)

best = paths[0][0]
best_index = 1
# for path in paths[1:]:
#     if path[0] < best:
#         best = path[0]
#         best_index = paths.index(path)

for step in range(len(paths[best_index][1])):
    c = corners[paths[best_index][1][step]]
    array[c[0],c[1]] = step - (10 * int(step / 10))

print(array)