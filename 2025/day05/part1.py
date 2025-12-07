raw_inputs = open("inputs.txt")
inputs = raw_inputs.readlines()

fresh_ingredient_id_ranges = [[int(range.split('-')[0]), int(range.split('-')[1])] for range in list(map(lambda s: s.strip(), inputs[:inputs.index('\n')]))]
ingredients = list(map(int, inputs[inputs.index('\n')+1:]))

fresh_ingredients = []

for ingredient in ingredients:
    for range in fresh_ingredient_id_ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            fresh_ingredients.append(ingredient)
            break

print(fresh_ingredients)

print(f"{len(fresh_ingredients)} of the available ingredient IDs are fresh.")

raw_inputs.close()