# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readline().split(' ')

for blinks in range(25):
    splitting = []
    for stone in range(len(contents)):
        # rule 1: value is 0 -> becomes 1
        if contents[stone]=='0':
            contents[stone] = '1'
        # rule 2: lenght of value is even -> two stones
        elif not len(contents[stone]) % 2:
            split_stones = [stone, str(int(contents[stone][:int(len(contents[stone])/2)])), str(int(contents[stone][int(len(contents[stone])/2):]))]
            splitting.append(split_stones)
        # rule 3: all other cases -> multiply by 2024
        else:
            contents[stone] = str(int(contents[stone]) * 2024)

    # split stones
    for stone in splitting[::-1]:
        contents[stone[0]] = stone[1]
        contents.insert(stone[0]+1, stone[2])

print(len(contents))