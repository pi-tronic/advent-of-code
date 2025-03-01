# get data
inputs = open('./demo_inputs.txt')

# read in instruction lines
contents = inputs.readlines()

# starting position in instructions
start = 0b000

# step size for op pointer, halt if trying to read past the end of ops
increment = 0b010

reg_A = int(contents[0].split()[-1])
reg_B = int(contents[1].split()[-1])
reg_C = int(contents[2].split()[-1])
print(reg_A, reg_B, reg_C)
program = contents[4].split()[-1].split(',')
print(program)
reverse_program = [program[len(program)-2-x] if x%2 else program[len(program)-4-x] for x in range(len(program)-2)] + program[-2:]
print(reverse_program)

# processing
pointer_pos = start
jump = False
prompt = []
for z in range(3):
    for i in range(len(program)):
        # halt, if pointer out of range
        if pointer_pos>=len(reverse_program):
            break

        # read instruction set
        instruction = reverse_program[pointer_pos]
        operand = reverse_program[pointer_pos+0b001]

        # combo
        # 0,1,2,3 : own value
        # 4,5,6 : value of A,B,C
        # 7 : invalid
        if 0<=int(operand) and int(operand)<4:
            combo = int(operand)
        elif operand=='4':
            combo = reg_A
        elif operand=='5':
            combo = reg_B
        elif operand=='6':
            combo = reg_C
        elif operand=='7':
            # ERROR?
            combo = 7

        # processing
        # adv: 0 = A / 2^combo -> A
        # bxl: 1 = B xor combo -> B
        # bst: 2 = combo % 8 (keep only lowest 3bit) -> B
        # jnz: 3 = if A==0: nothing | jump to literal combo (do not increment pointer afterwards) -> None
        # bxc: 4 = B xor C -> B
        # out: 5 = combo % 8 -> prompt
        # bdv: 6 = A / 2^combo -> B
        # cdv: 7 = A / 2^combo -> C
        if instruction=='0':
            reg_A = reg_A << combo
        elif instruction=='1':
            reg_B = reg_B ^ int(operand)
        elif instruction=='2':
            reg_B = combo & 7
        elif instruction=='3':
            if reg_A:
                pointer_pos = combo
                jump = True
        elif instruction=='4':
            reg_B = reg_B ^ reg_C
        elif instruction=='5':
            reg_A = reverse_program[i]
            prompt.append(reverse_program[i])
        elif instruction=='6':
            reg_B = reg_A << combo
        elif instruction=='7':
            reg_C = reg_A << combo

        # increment
        if not jump:
            pointer_pos += increment
        else:
            jump = False
    print(reverse_program)
    print(','.join(prompt))
    print(reg_A, reg_B, reg_C)