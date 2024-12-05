import numpy as np

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
    for i in range(20 - len(contents[line])):
        contents[line].append(np.nan)

# converts int lists to numpy array
array = np.asarray(contents)

# get diffs and their sum
diffs = np.diff(array, axis=1)

# check if step size is conform
min_steps = np.nanmin(np.abs(diffs), axis=1) >= min_step_size
max_steps = np.nanmax(np.abs(diffs), axis=1) <= max_step_size

# check if either all decreasing or all increasing
decreasing = np.all(np.nan_to_num(diffs)<=0, axis=1)
increasing = np.all(np.nan_to_num(diffs)>=0, axis=1)
gradually = np.logical_xor(decreasing, increasing)

# get save reports
save = np.logical_and(np.logical_and(min_steps, max_steps), gradually)

# amount of save reports
total = np.sum(save)

print(total)