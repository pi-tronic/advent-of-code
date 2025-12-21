from tqdm import tqdm

inputs = open("inputs.txt")

button_presses = 0

def get_score(joltage_diagram, joltage_levels):
    for current_joltage, joltage in zip(joltage_diagram, joltage_levels):
        if current_joltage > joltage:
            return -1
    return sum(current_joltage / joltage for current_joltage, joltage in zip(joltage_diagram, joltage_levels)) / len(joltage_diagram)

def update_joltage(joltage_diagram, indices):
    return [joltage + 1 * (i in indices) for i,joltage in enumerate(joltage_diagram)]

def find_solution(depth):
    # solve the joltage
    states = [[joltage_diagram, get_score(joltage_diagram, joltage_levels)]]
    next_states = []
    for step in tqdm(range(depth), position=1):
        for state in states:
            # check every button option and calculate their score
            for option in buttons:

                # get next state
                next_state = update_joltage(state[0], option)
                score = get_score(next_state, joltage_levels)

                # if the state is desired (score = 1), return the current step (how oten the buttons where switched)
                if score == 1.0:
                    return step + 1
                elif score < 0:
                    continue

                # add the results to the next states
                next_states.append([next_state, score])

        # set next_states to states
        states = next_states.copy()
        next_states.clear()

    return -1

for line in tqdm(inputs.readlines(), position=0):
    # extract and setup data
    line = line[:-1].split()
    buttons = [list(map(int, button[1:-1].split(','))) for button in line[1:-1]]
    joltage_levels = list(map(int, line[-1][1:-1].split(",")))
    joltage_diagram = [0 for i in range(len(joltage_levels))]

    # print(joltage_diagram, update_joltage(joltage_diagram, buttons[1]))
    # print(get_score(joltage_levels, joltage_levels))

    steps = find_solution(100)
    if steps < 0:
        print(f"ERROR at {line}!")

    button_presses += steps

print(button_presses)

inputs.close()