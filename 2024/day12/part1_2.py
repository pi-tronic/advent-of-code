import numpy as np

# get data
inputs = open('./demo_inputs.txt')

# read in instruction lines
contents = inputs.readlines()

# create id array to store ids of contents
identifier = np.array([list(contents[0][:-1])])

for row in range(1, len(contents)):
    identifier = np.concatenate((identifier,[np.array(list(contents[row][:-1]))]), axis=0)

indices = np.argwhere(identifier=='I')
print(np.all(np.array([4,6]) in indices))
#
# searched_inds = []
# next_points = [list(indices[0])]
# for point in next_points:
#     searched_inds_ = [point]
#     next_points_ = []
    
#     if 

#     for point_ in searched_inds_:
#         searched_inds.append(point_)
