import numpy as np

# get data
inputs = open('./inputs.txt')

# convert strings to int lists
contents = inputs.readlines()
for line in range(len(contents)):
    contents[line] = [int(x) for x in contents[line].split(' ') if x]

# converts int lists to numpy array
array = np.asarray(contents)

# sort columns
array = np.sort(array, axis=0)

# get diffs and their sum
diffs = np.diff(array, axis=1)
total = np.sum(np.abs(diffs))

print(total)