def filterbyvalue(value, seq):
   return [x for x in seq if x!=value]

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readline()[:-1]

# decode filesystem
filesystem = []
for block_id in range(0, int(len(contents)/2)+1):
    for size in range(int(contents[block_id*2])):
        filesystem.append(str(block_id))
    try:
        for size in range(int(contents[block_id*2+1])):
            filesystem.append('.')
    except IndexError:
        break

# free right disk space
while True:
    # print(''.join(filesystem))
    if len(list(filter(None, ''.join(filesystem).split('.'))))>1:
        # move left
        first_free = filesystem.index('.')
        last_block = len(filesystem) - filesystem[::-1].index(filterbyvalue('.', filesystem)[-1]) - 1
        filesystem[first_free] = filesystem[last_block]
        filesystem[last_block] = '.'
    else:
        break

# calculate checksum
total = 0
check_ids = filterbyvalue('.', filesystem)
for pos in range(len(check_ids)):
    total += pos * int(check_ids[pos])

print(total)