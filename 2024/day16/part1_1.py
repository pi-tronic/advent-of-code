import numpy as np
from find_graph import find_graph
from solve_graph import solve_graph

file_path = './my_file01.txt'

edges, lenghts, orientation, nodes, start, end = find_graph(file_path)
paths = solve_graph(start, end, nodes, edges, lenghts, orientation)

print(paths)

print('\n', min(paths))