import numpy as np

# get data
inputs = open('./inputs.txt')

# convert strings to int lists
contents = inputs.readlines()
for line in range(len(contents)):
    contents[line] = [int(x) for x in contents[line].split(' ') if x]

# converts int lists to numpy array
array = np.asarray(contents)

# get amounts of ids and convert to dictionary
unique, counts = np.unique(array[:,1], return_counts=True)
right_list = dict(zip(unique, counts))

# function to get value based on amount in right list
def weight(a):
    try:
        return a[0] * right_list[a[0]]
    except KeyError:
        return 0

# apply function to get all values
weights = np.apply_along_axis(weight, 1, array)

# get sum
total = np.sum(weights)

print(total)