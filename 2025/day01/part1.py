inputs = open("inputs.txt")

range_max = 99
range_min = 0

dial = 50
ceros = 0

for line in inputs:
    direction = line[0]
    number = int(line[1:-1])
    
    if direction=="R":
        dial = (dial + number) % 100
    elif direction=="L":
        dial = (dial - number) % 100
    
    if dial==0:
        ceros += 1

print(ceros)

inputs.close()