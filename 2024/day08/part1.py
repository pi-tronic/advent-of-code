# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

# boundaries
bound_col = len(contents[0])-1
bound_row = len(contents)

def anti(coord_0, coord_1):
    delta_row = coord_1[0]-coord_0[0]
    delta_col = coord_1[1]-coord_0[1]
    if coord_0[0]-delta_row >= 0 and coord_0[0]-delta_row < bound_row and coord_0[1]-delta_col >= 0 and coord_0[1]-delta_col < bound_col:
        anti_coord_0 = [coord_0[0]-delta_row, coord_0[1]-delta_col]
    else:
        anti_coord_0 = None
    if coord_1[0]+delta_row >= 0 and coord_1[0]+delta_row < bound_row and coord_1[1]+delta_col >= 0 and coord_1[1]+delta_col < bound_col:
        anti_coord_1 = [coord_1[0]+delta_row, coord_1[1]+delta_col]
    else:
        anti_coord_1 = None
    return anti_coord_0, anti_coord_1

# get individual frequencies
frequencies = {}
for line in range(len(contents)):
    for letter in range(len(contents[line])-1):
        if contents[line][letter] != '.':
            if not frequencies.get(contents[line][letter]):
                frequencies.update({contents[line][letter]: [[line, letter]]})
            else:
                frequencies.get(contents[line][letter]).append([line, letter])

antinodes = []
for freq in frequencies:
    coords = frequencies.get(freq)
    for coord_0 in range(len(coords)):
        for coord_1 in range(coord_0 + 1, len(coords)):
            antinode_0, antinode_1 = anti(coords[coord_0], coords[coord_1])
            if antinode_0 and antinode_0 not in antinodes:
                antinodes.append(antinode_0)
            if antinode_1 and antinode_1 not in antinodes:
                antinodes.append(antinode_1)

print(len(antinodes))

# for node in antinodes:
#     contents[node[0]] = contents[node[0]][:node[1]] + '#' + contents[node[0]][node[1]+1:]
# for row in contents:
#     print(row[:-1])