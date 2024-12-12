import numpy as np

# get data
inputs = open('./demo_inputs.txt')

# read in instruction lines
contents = inputs.readlines()

# create id array to store ids of contents
identifier = np.zeros((len(contents), len(contents[0])-1))

def new_id(old_id):
    return old_id + 1

# get coherent blocks
# pass 1
current_id = 0
for row in range(len(contents)):
    for col in range(len(contents[0])-1):
        if contents[row][col] == contents[row-1][col] and row-1 >= 0:
            identifier[row,col] = identifier[row-1,col]
        elif contents[row][col] == contents[row][col-1] and col-1 >= 0:
            identifier[row,col] = identifier[row,col-1]
        else:
            current_id = new_id(current_id)
            identifier[row,col] = current_id
# pass 2
for row in range(len(contents)-1,-1,-1):
    for col in range(len(contents[0])-2,-1,-1):
        try:
            if contents[row][col] == contents[row+1][col] and row+1 < len(contents):
                identifier[row,col] = identifier[row+1,col]
        except IndexError:
            pass
        try:
                if contents[row][col] == contents[row][col+1] and col+1 < len(contents[0])-1:
                    identifier[row,col] = identifier[row,col+1]
        except IndexError:
            pass

print(identifier)

total = 0

# count size per block and multiply it with the outline
for block_id in range(1, current_id+1):
    # size
    size = np.shape(identifier[identifier==block_id])[0]
    # outline lenght
    y, x = np.where(identifier==block_id)
    adjacent = len(np.diff(np.sort(y))[np.diff(np.sort(y))==0]) + len(np.diff(np.sort(x))[np.diff(np.sort(x))==0])
    outline = size*4 - adjacent*2
    total += size * outline
    print(size, outline, size * outline)

print(total)