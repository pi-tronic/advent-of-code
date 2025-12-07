inputs = open("inputs.txt")

# how many batteries are to be turned on
n = 2

total_joltage = 0

for line in inputs:
    bank = list(map(int, line[:-1]))
    last_index = 0
    joltage = 0
    # find the highest possible joltage
    for i in range(n):
        joltage += max(bank[last_index:len(line[:-1])-n+i+1]) * 10**(n-i-1)
        last_index = bank[last_index:len(line[:-1])-n+i+1].index(max(bank[last_index:len(line[:-1])-n+i+1])) + 1
    total_joltage += joltage
    print(line[:-1], joltage)

print(total_joltage)

inputs.close()