import re

# is multiplication enabled
enabled = True

# get data
inputs = open('./inputs.txt')

# read in instruction lines
contents = inputs.readlines()

# mul pattern
mul = re.compile(r'mul\(\d*,\d*\)')
# do pattern
do = re.compile(r"do(n't)?\(\)")
# int pattern
val = re.compile(r'(\d*),(\d*)')

total = 0

# go through all lines
for line in contents:
    # keep going through the instructions
    while True:
        # find next
        operation = re.search(mul, line)
        action = re.search(do, line)

        # skip line if there is nothing to be done 
        if not operation and enabled or not action and not enabled:
            break

        # check for do and don't to en-/disable calculation
        if action:
            if not operation or not enabled:
                if action.group(1) == "n't" and enabled:
                    enabled = False
                elif not action.group(1) and not enabled:
                    enabled = True
                line = line[action.span()[1]:]
                continue
            elif action.span()[0] < operation.span()[0]:
                if action.group(1) == "n't" and enabled:
                    enabled = False
                elif not action.group(1) and not enabled:
                    enabled = True
                line = line[action.span()[1]:]
                continue

        # execute multiplication, if possible
        if enabled and operation:
            # do math
            values = re.findall(val, operation.group())
            values = list(values[0])
            total += int(values[0]) * int(values[1])
            # cut string
            line = line[operation.span()[1]:]


print(total)