inputs = open("demo_inputs.txt")

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
    for step in range(depth):
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

for line in inputs.readlines():
    # extract and setup data
    line = line[:-1].split()
    buttons = [list(map(int, button[1:-1].split(','))) for button in line[1:-1]]
    joltage_levels = list(map(int, line[-1][1:-1].split(",")))
    joltage_diagram = [0 for i in range(len(joltage_levels))]

    dependence = dict()
    for i in list(range(len(joltage_levels))):
        dependence.update({i : [index for button in buttons for index in button].count(i)})
    print(dependence)

    next_button = buttons[[sum(dependence[index] for index in button) / len(button) for button in buttons].index(min(sum(dependence[index] for index in button) / len(button) for button in buttons))]
    print(next_button)

    print(joltage_levels, next_button)


    for i in range(6):
        a = [1 if level - joltage > 0 else 0 for joltage, level in zip(joltage_diagram, joltage_levels)]
        
        print(joltage_diagram, joltage_levels, a)

        joltage_diagram = update_joltage(joltage_diagram, buttons[1])


    # steps = find_solution(100)
    # if steps < 0:
    #     print(f"ERROR at {line}!")

    # button_presses += steps

    break

print(button_presses)

inputs.close()