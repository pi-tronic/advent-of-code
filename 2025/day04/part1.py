import numpy as np

inputs = open("inputs.txt")

grid = []
for line in inputs:
    grid.append(list(line[:-1]))
grid = np.asarray(grid)
x, y = grid.shape
print(grid)

# check every '@' in the grid, if it has fewer than four adjacent '@' (=roll of paper)
# get locations of '@'
locations = np.argwhere(grid=='@')
reachable_locations = []
# check the adjacent cells
for location in locations:
    indices = np.array([
        [location[0]-1, location[1]-1],
        [location[0]-1, location[1]],
        [location[0]-1, location[1]+1],
        [location[0],   location[1]-1],
        [location[0],   location[1]+1],
        [location[0]+1, location[1]-1],
        [location[0]+1, location[1]],
        [location[0]+1, location[1]+1]
    ])
    indices_in_bounds = np.argwhere(np.all((indices >= 0) & (indices < x), axis=1)).flatten()
    adjacent_rolls = 0
    for index in indices[indices_in_bounds]:
        # print(index, grid[tuple(index)])
        if grid[tuple(index)] == '@':
            adjacent_rolls += 1
    if adjacent_rolls < 4:
        reachable_locations.append(location)

# convert '@' to 'x', if it is reachable
for location in reachable_locations:
    grid[tuple(location)] = 'x'
print(grid)

print(f"There are {len(reachable_locations)} rolls of paper that can be accessed by a forklift.")

inputs.close()