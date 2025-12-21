import numpy as np
from tqdm import tqdm

inputs = open("inputs.txt")

# prepare directed graph
start_device = "svr"
dac = "dac"
fft = "fft"
reactor = "out"
connections = dict([[line[:-1].split(':')[0], line[:-1].split(':')[1].split()] for line in inputs.readlines()])
nodes = list(connections.keys())
edges = np.array([[node, connection] for node in nodes for connection in connections[node]])

inputs.close()

def get_value(connection, wanted):
    value = sum(cashing[conn] if cashing[conn] > 0 or conn not in wanted else get_value(conn, wanted) for conn in connections[connection])
    return value

# walk multiple combinations (svr_fft, svr_dac, fft_dac, fft_out, dac_fft, dac_out)
paths = [["svr", "fft"], ["svr", "dac"], ["fft", "dac"], ["fft", "out"], ["dac", "fft"], ["dac", "out"]]
values = []

for path in paths:
    # walk graph in reverse with cashing
    cashing = dict([[node, 0] for node in nodes] + [[reactor, 0]])

    # setup
    cashing[path[1]] = 1
    possible = True

    # reverse order
    reverse_order = []
    branches = [path[1]]
    while True:
        try:
            next_layer = np.unique(np.concatenate([edges[edges[:,1] == branch][:,0] for branch in branches])).tolist()
        except ValueError:
            possible = False
            break
        branches = next_layer
        # add to order
        for element in next_layer:
            if element not in reverse_order:
                reverse_order.append(element)
        if path[0] in next_layer:
            break

    if possible:
        for element in tqdm(reverse_order):
            if cashing[element] == 0:
                cashing[element] = get_value(element, reverse_order)

            if element == path[0]:
                break

    print(cashing[path[0]])
    values.append(cashing[path[0]])

print(f"svr -> fft -> dac -> out : {values[0]}, {values[2]}, {values[5]}\t\t\t\t= {values[0]*values[2]*values[5]}")
print(f"svr -> dac -> fft -> out : {values[1]}, {values[4]}, {values[3]}\t\t= {values[1]*values[4]*values[3]}")
print(values[0]*values[2]*values[5] + values[1]*values[4]*values[3])