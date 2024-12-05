import re

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

# mul pattern
mul = re.compile(r'mul\(\d*,\d*\)')
# int pattern
val = re.compile(r'(\d*),(\d*)')

total = 0

# go through all lines
for line in contents:
    # find all instances
    res = re.findall(mul, line)

    # do math
    for m in res:
        values = re.findall(val, m)
        values = list(values[0])
        total += int(values[0]) * int(values[1])
    
print(total)