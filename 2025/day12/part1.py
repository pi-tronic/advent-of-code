import numpy as np

inputs = open("demo_inputs.txt")
lines = [line[:-1] for line in inputs.readlines()]
inputs.close()

# shapes
empty = [-1] + [i for i, x in enumerate(lines) if x == ""]
shapes = [np.array([[1 if el=='#' else 0 for el in line] for line in lines[empty[i]+2:empty[i+1]]]) for i in range(len(empty)-1)]
# regions and shape list
regions = [[list(map(int, line.split(':')[0].split('x'))), list(map(int, line.split(':')[1].split()))] for line in lines[empty[-1]+1:]]

for region in regions:
    grid = np.zeros((region[0][1],region[0][0]))
    for i, r in enumerate(region[1]):
        if r > 0:
            for line in shapes[i]:
                print(line)
            for s in range(r):
                # find starting point
                starting_points = np.argwhere(grid == 0)
                starting_points = starting_points[np.all([starting_points[:,0] <= grid.shape[1] - 3, starting_points[:,1] <= grid.shape[0] - 3], axis=0)]
                print(starting_points)
                if starting_points.shape[0]:
                    for starting_point in starting_points:
                        # try with all rotations
                        try:
                            if np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + shapes[i]) <= 1:
                                grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += shapes[i]
                                break
                        except ValueError:
                            print(42, starting_point, grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3])
                            break
                        if np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + shapes[i].T) <= 1:
                            grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += shapes[i].T
                            break
                        elif np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + np.flip(shapes[i], axis=1)) <= 1:
                            grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += np.flip(shapes[i], axis=1)
                            break
                        elif np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + np.flip(shapes[i], axis=1).T) <= 1:
                            grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += np.flip(shapes[i], axis=1).T
                            break
                        elif np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + np.flip(shapes[i], axis=0)) <= 1:
                            grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += np.flip(shapes[i], axis=0)
                            break
                        elif np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + np.flip(shapes[i], axis=0).T) <= 1:
                            grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += np.flip(shapes[i], axis=0).T
                            break
                        elif np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + np.flip(np.flip(shapes[i], axis=0), axis=1)) <= 1:
                            grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += np.flip(np.flip(shapes[i], axis=0), axis=1)
                            break
                        elif np.max(grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] + np.flip(np.flip(shapes[i], axis=0), axis=1).T) <= 1:
                            grid[starting_point[0]:starting_point[0]+3,starting_point[1]:starting_point[0]+3] += np.flip(np.flip(shapes[i], axis=0), axis=1).T
                            break
                        # if no solution found, try again with next free point

                    # if no solution after all starting points, break for now

            print(grid)