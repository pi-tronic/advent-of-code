import numpy as np

inputs = open("inputs.txt")
# create the grid from the inputs
grid = np.array(list(map(lambda s: list(s.strip()), inputs.readlines())))
width = grid.shape[1]
# get the first set of starting points
starting_points = np.argwhere(grid == 'S')
next_starting_points = []
splits = []

# repeat, until no splitters are found
while True:
    # only look at the points in the highest row, so push the rest to another iteration
    highest_row = np.min(starting_points[:,0])
    if starting_points[np.argwhere(starting_points[:,0] > highest_row)].shape[0] != 0:
        next_starting_points = [x[0] for x in starting_points[np.argwhere(starting_points[:,0] > highest_row)].tolist()]
    # loop through all the remaining starting points
    for starting_point in starting_points[starting_points[:,0]==highest_row]:
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
                if all(coord>=0 for coord in point) and all(coord<width for coord in point) and point not in next_starting_points:
                    next_starting_points.append(point)
            # add unique splits to list
            if [next_splitter, starting_point[1]] not in splits:
                splits.append([next_splitter, starting_point[1]])
        # if no splitter is found, just do nothing

    # set next starting points and clear temporary list
    if len(next_starting_points):
        starting_points = np.array(next_starting_points)
        next_starting_points.clear()
    # if there are no splitters found, the loop stops
    else:
        break

print(f"A tachyon beam is split a total of {len(splits)} times.")

inputs.close()