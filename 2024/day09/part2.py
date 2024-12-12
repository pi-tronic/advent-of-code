def filterbyvalue(value, seq):
   return [x for x in seq if x==value]

def get_consecutive(value, lenght, seq):
    amount = 0
    for index in range(len(seq)):
        if seq[index]==value:
            amount += 1
        elif seq[index]!=value and amount!=0:
            amount = 0
        
        if amount >= lenght:
            return index - lenght + 1
    return -1

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
        max_id = block_id
        break

# free right disk space
for block_id in range(max_id,-1,-1):
    # print(block_id, ''.join(filesystem))
    try:
        block_index = filesystem.index(str(block_id))
    except ValueError:
        continue
    block_lenght = len(filterbyvalue(str(block_id), filesystem))
    free_index = get_consecutive('.', block_lenght, filesystem[:block_index])

    if free_index!=-1:
        # move
        for i in range(block_lenght):
            filesystem[free_index+i] = str(block_id)
            filesystem[block_index+i] = '.'

# calculate checksum
total = 0
for pos in range(len(filesystem)):
    if filesystem[pos] != '.':
        total += pos * int(filesystem[pos])

print(total)