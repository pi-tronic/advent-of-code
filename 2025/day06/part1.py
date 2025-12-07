import numpy as np

inputs = open("inputs.txt")
lines = inputs.readlines()
math_problems = np.array(list(list(map(int, line.split())) for line in list(map(lambda s: s.strip(), lines))[:-1]))
operators = lines[-1].split()

grand_total = 0

for i, operator in enumerate(operators):
    if operator=='+':
        grand_total += np.sum(math_problems[:,i])
    elif operator=='*':
        grand_total += np.prod(math_problems[:,i])

print(f"The grand total is {grand_total}.")

inputs.close()