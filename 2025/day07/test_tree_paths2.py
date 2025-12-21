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

V = {int(node) : None for node in nodes}
L = {int(node) : edges[edges[:,0] == node, 1].tolist() for node in nodes}

for node in np.flip(nodes):
    if L[node]:
        V[node] = sum(V[child] for child in L[node])
    else:
        V[node] = 1

print(V[0])