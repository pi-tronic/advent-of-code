import numpy as np

inputs = open("inputs.txt")
# create the grid from the inputs
grid = np.array(list(map(lambda s: list(s.strip()), inputs.readlines())))
width = grid.shape[1]
# get the first set of starting points
starting_points = list(map(lambda s: list(s + [-1]), np.argwhere(grid == 'S').tolist()))
next_starting_points = []

# build a directional graph in here
nodes = np.argwhere(grid == '^').tolist()
visited_nodes = []
nodes.append('EOL')
edges = []

# repeat, until no splitters are found
while True:
    # loop through all starting points
    for starting_point in starting_points:
        # extract column
        current_column = np.argwhere(grid[starting_point[0]+1:,starting_point[1]] == '^')
        # check, if there was found a splitter
        if current_column.shape[0] != 0:
            # find next splitter (index)
            next_splitter = current_column[0,0] + starting_point[0] + 1
            # create starting points to the left and the right of the splitter
            starting_point_left = [next_splitter, starting_point[1] - 1]
            starting_point_right = [next_splitter, starting_point[1] + 1]
            # >=width or <0 is out of bounds
            for point in [starting_point_left, starting_point_right]:
                if all(coord>=0 for coord in point) and all(coord<width for coord in point):
                    if point + [nodes.index([next_splitter, starting_point[1]])] not in next_starting_points and point + [nodes.index([next_splitter, starting_point[1]])] not in visited_nodes:
                        next_starting_points.append(point + [nodes.index([next_splitter, starting_point[1]])])
                        visited_nodes.append(point + [nodes.index([next_splitter, starting_point[1]])])
                    # create edges
                    if starting_point[2] >= 0:
                        if starting_point[1] < nodes[starting_point[2]][1]:
                            if [starting_point[2], nodes.index([next_splitter, starting_point[1]]), 0] not in edges:
                                edges.append([starting_point[2], nodes.index([next_splitter, starting_point[1]]), 0])
                        else:
                            if [starting_point[2], nodes.index([next_splitter, starting_point[1]]), 1] not in edges:
                                edges.append([starting_point[2], nodes.index([next_splitter, starting_point[1]]), 1])
        # if no splitter is found, set to EOL
        else:
            # create edges
            if starting_point[2] >= 0:
                if starting_point[1] < nodes[starting_point[2]][1]:
                    edges.append([starting_point[2], nodes.index('EOL'), 0])
                else:
                    edges.append([starting_point[2], nodes.index('EOL'), 1])

    # set next starting points and clear temporary list
    if len(next_starting_points):
        starting_points = next_starting_points.copy()
        next_starting_points.clear()
    # if there are no splitters found, the loop stops
    else:
        break

#### now that the graph is created, go through it

nodes = np.array(range(len(nodes)))
edges = np.array(edges)

V = {int(node) : None for node in nodes}
L = {int(node) : edges[edges[:,0] == node, 1].tolist() for node in nodes}

for node in np.flip(nodes):
    if L[node]:
        V[node] = sum(V[child] for child in L[node])
    else:
        V[node] = 1

print(V[0])