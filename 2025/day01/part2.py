from math import ceil, floor

inputs = open("inputs.txt")

range_max = 99
range_min = 0

dial = 50
ceros = 0

print(f"The dial starts by pointing at {dial}.")

for line in inputs:
    direction = line[0]
    number = int(line[1:-1])

    hits = 0

    if direction=="R":
        hits = floor((number + dial) / (range_max + 1))
        dial = (dial + number) % 100
    elif direction=="L":
        hits = floor((number + (100 - dial)) / (range_max + 1))
        if hits and not dial:
            hits -= 1
        dial = (dial - number) % 100

    if hits and dial!=0:
        print(f"The dial is rotated {line[:-1]} to point at {dial}; during this rotation, it points at 0 {hits}x.")
    else:
        print(f"The dial is rotated {line[:-1]} to point at {dial}.")

    ceros += hits

print(ceros)

inputs.close()

# part 2 greater than 6158