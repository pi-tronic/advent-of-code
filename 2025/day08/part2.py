import numpy as np

inputs = open("inputs.txt")

coords = np.array([list(map(int, line[:-1].split(','))) for line in inputs.readlines()])
squared = np.sum(coords**2, axis=1)
matrix = np.matmul(coords, coords.T)
dists = np.sqrt(squared.reshape(-1, 1) - 2*matrix + squared)
dists = np.triu(dists)
dists[dists == 0] = np.inf
n = dists.shape[0]

circuits = np.empty((0,3))
freed_indices = []
latest_circuit_index = 0

for i in range(100000):
    if np.min(dists) == np.inf:
        print("ATTENTION! All junction boxes are connected.")
        break
    # find closest junktion boxes
    closest_boxes = np.argwhere(dists == np.min(dists))
    # check if at least on was found
    if closest_boxes.shape[0]:
        dists[closest_boxes[0,0], closest_boxes[0,1]] = np.inf
        # add first pair to correct circuit, and combine circuits if they become connected
        containing_circuits = np.append(np.unique(circuits[np.unique(np.argwhere(circuits[:,:2] == closest_boxes[0,0])[:,0])][:,2]), np.unique(circuits[np.unique(np.argwhere(circuits[:,:2] == closest_boxes[0,1])[:,0])][:,2]))
        if containing_circuits.shape[0]:
            if containing_circuits.shape[0] == 1:
                added_nodes = np.unique(closest_boxes)
            if containing_circuits.shape[0] == 2:
                added_nodes = np.unique(np.append(closest_boxes, circuits[np.argwhere(circuits[:,2] == np.max(containing_circuits)),:2]))
                if np.all(containing_circuits[0] == containing_circuits[1]):
                    # print("oh no! there was a connection between two nodes already in the same circuit")
                    continue
                else:
                    freed_indices.append(np.max(containing_circuits))
                    circuits[np.argwhere(circuits[:,2] == np.max(containing_circuits)),2] = np.min(containing_circuits)
            circuits = np.append(circuits, [np.append(closest_boxes, np.min(containing_circuits))], axis=0)

            # delete all connections between the node added and all other nodes in the circuit
            # yx--z--z
            # | 0+++++  -> x > y
            # z .0o++o
            # | ..0+++
            # other_nodes = np.unique(circuits[np.argwhere(circuits[:,2] == np.min(containing_circuits)),:2])
            # nodes_to_set_inf = np.flip(np.sort(np.concatenate([[np.repeat(added_nodes, other_nodes.shape[0])], [np.tile(other_nodes, added_nodes.shape[0])]], axis=0).T), axis=1).T.astype(int)
            # print(nodes_to_set_inf)
            # dists[nodes_to_set_inf[1], nodes_to_set_inf[0]] = np.inf

        else:
            if freed_indices:
                circuits = np.append(circuits, [np.append(closest_boxes, freed_indices[0])], axis=0)
                del freed_indices[0]

            else:
                circuits = np.append(circuits, [np.append(closest_boxes, latest_circuit_index)], axis=0)
                latest_circuit_index += 1

    if len(set(circuits[circuits[:,2] == 0, :2].flatten())) == n:
        result = np.prod(coords[closest_boxes,0])
        break

# unique_circuits, amount = np.unique(circuits[:,2], return_counts=True)

print(result)

inputs.close()