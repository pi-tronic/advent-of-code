import numpy as np
from tqdm import tqdm

inputs = open("inputs.txt")

# prepare directed graph
start_device = "you"
reactor = "out"
connections = dict([[line[:-1].split(':')[0], line[:-1].split(':')[1].split()] for line in inputs.readlines()])
nodes = list(connections.keys())
edges = np.array([[node, connection] for node in nodes for connection in connections[node]])

inputs.close()

# walk graph in reverse with cashing
cashing = dict([[node, 0] for node in nodes] + [[reactor, 1]])

# reverse order
reverse_order = []
branches = [reactor]
while True:
    next_layer = np.unique(np.concatenate([edges[edges[:,1] == branch][:,0] for branch in branches])).tolist()
    branches = next_layer
    # add to order
    for element in next_layer:
        if element not in reverse_order:
            reverse_order.append(element)
    if start_device in next_layer:
        break

def get_value(connection):
    value = sum(cashing[conn] if cashing[conn] > 0 else get_value(conn) for conn in connections[connection])
    return value

for element in tqdm(reverse_order):
    if cashing[element] == 0:
        cashing[element] = get_value(element)

    if element == start_device:
        break

print(cashing)
print(cashing[start_device])

