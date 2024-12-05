import numpy as np

# max levels
levels = 8

# define step sizes
min_step_size = 1
max_step_size = 3

# get data
inputs = open('./inputs.txt')

# convert strings to int lists
contents = inputs.readlines()
for line in range(len(contents)):
    contents[line] = [int(x) for x in contents[line].split(' ') if x]
    # add nan for shape of array, nan has to be handled later
    for i in range(levels - len(contents[line])):
        contents[line].append(np.nan)

# converts int lists to numpy array
array = np.asarray(contents)

# storage for results
storage = np.zeros((array.shape))

# brute force through all
for col in range(levels):
    temp_array = array.copy()
    temp_array = np.delete(temp_array, col, axis=1)

    # get diffs and their sum
    diffs = np.diff(temp_array, axis=1)

    # check if step size is conform
    min_steps = np.nanmin(np.abs(diffs), axis=1) >= min_step_size
    max_steps = np.nanmax(np.abs(diffs), axis=1) <= max_step_size

    # check if either all decreasing or all increasing
    decreasing = np.all(np.nan_to_num(diffs)<=0, axis=1)
    increasing = np.all(np.nan_to_num(diffs)>=0, axis=1)
    gradually = np.logical_xor(decreasing, increasing)

    # get save reports
    save = np.logical_and(np.logical_and(min_steps, max_steps), gradually)

    # store
    storage[:,col] = save

# get all reports save in certain conditions of removing one level
save = np.any(storage, axis=1)

# amount of save reports
total = np.sum(save)

print(total)