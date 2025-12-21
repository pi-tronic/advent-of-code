import numpy as np

nodes = np.array(range(7))
edges = np.array([
    [0,1],
    [0,2],
    [1,3],
    [1,4],
    [2,4],
    [2,5],
    [3,6],
    [3,6],
    [4,6],
    [4,6],
    [5,6],
    [5,6]
])

root_node = nodes[0]
eol_node = nodes[-1]

paths = []

index = 0
offset = [0]
node_path = [root_node]
edge_path = []

while True:
    # get edge with offset from current node
    next_edge = np.argwhere(edges[:,0] == node_path[index])[0,0] + offset[index]
    # if this edge does not start from the current edge, increase offset at index-1 by one and set offset at own index to 0 | if index-1 < 0: end.
    if next_edge < edges.shape[0]:
        edge = edges[next_edge]
        if edge[0] != node_path[index]:
            offset[index - 1] += 1
            del offset[index]
            del node_path[index]
            del edge_path[index - 1]
            index -= 1
        else:
            edge_path.append(next_edge)
            # if next node is eol_node, increase the offset at index by one
            if edge[1] == eol_node:
                offset[index] += 1
                paths.append(edge_path.copy())
                del edge_path[-1]
            else:
                node_path.append(edge[1])
                offset.append(0)
                index += 1
    else:
        break

print(paths)