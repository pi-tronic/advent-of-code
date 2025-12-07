import numpy as np

inputs = open("inputs.txt")
lines = inputs.readlines()
math_problems = lines[:-1]
operators = lines[-1].split()
j, n = 0, len(math_problems)
numbers = []

grand_total = 0

print(math_problems)

for i, operator in enumerate(operators):
    while True:
        next_number = ''.join(math_problems[k][j] for k in range(n)).strip()
        if next_number:
            numbers.append(int(next_number))
        else:
            print(operator, numbers)
            if operator=='+':
                grand_total += np.sum(np.asarray(numbers))
            elif operator=='*':
                grand_total += np.prod(np.asarray(numbers))
            numbers.clear()
            j += 1
            break
        j += 1

print(f"The grand total is {grand_total}.")

inputs.close()