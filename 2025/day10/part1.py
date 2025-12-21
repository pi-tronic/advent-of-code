inputs = open("inputs.txt")

button_presses = 0

def get_score(light_diagram, lights):
    return sum(1 for i,light in enumerate(light_diagram) if light==1 and i in lights or light==0 and i not in lights) / len(light_diagram)

def flip_buttons(light_diagram, indices):
    return [1 if light == 0 and i in indices or light == 1 and i not in indices else 0 for i,light in enumerate(light_diagram)]

def find_solution(depth):
    # solve the lights
    states = [[light_diagram, get_score(light_diagram, lights), None]]
    next_states = []
    for step in range(depth):
        for state in states:
            # check every button option and calculate their score
            for i, option in enumerate(buttons):
                # skip, if the same buttons would be pressed (in other words undoing the last changes)
                if i == state[2]:
                    continue

                # get next state
                next_state = flip_buttons(state[0], option)
                score = get_score(next_state, lights)

                # if the state is desired (score = 1), return the current step (how oten the buttons where switched)
                if score == 1.0:
                    return step + 1

                # add the results to the next states
                next_states.append([next_state, score, i])

        # set next_states to states
        states = next_states.copy()
        next_states.clear()

    return -1

for line in inputs.readlines():
    # extract and setup data
    line = line[:-1].split()
    light_diagram = line[0][1:-1]
    lights = [i for i, light in enumerate(light_diagram) if light == '#']
    light_diagram = [0 for i in range(len(light_diagram))]
    buttons = [list(map(int, button[1:-1].split(','))) for button in line[1:-1]]
    joltage_levels = list(map(int, line[-1][1:-1].split(",")))

    steps = find_solution(100)
    if steps < 0:
        print(f"ERROR at {line}!\nButtons pressed until now: {button_presses}")

    button_presses += steps

print(button_presses)

inputs.close()