import numpy as np

raw_inputs = open("inputs.txt")
inputs = raw_inputs.readlines()

fresh_ingredient_id_ranges = np.array([[int(range.split('-')[0]), int(range.split('-')[1])] for range in list(map(lambda s: s.strip(), inputs[:inputs.index('\n')]))])
fresh_ingredient_ids_count = 0
fresh_ingredient_id_ranges.sort(axis=0)
print(fresh_ingredient_id_ranges)
id_ranges_to_delete = []

for i in range(len(fresh_ingredient_id_ranges) - 1):
    # if own end is greater or equal to start of next: overwrite next beginning with own beginning and check if own end is greater than next end, if true overwrite it too, then mark own index to be removed
    if fresh_ingredient_id_ranges[i,1] >= fresh_ingredient_id_ranges[i+1,0]:
        fresh_ingredient_id_ranges[i+1,0] = fresh_ingredient_id_ranges[i,0]
        if fresh_ingredient_id_ranges[i,1] > fresh_ingredient_id_ranges[i+1,1]:
            fresh_ingredient_id_ranges[i+1,1] = fresh_ingredient_id_ranges[i,1]
        id_ranges_to_delete.append(i)

# delete removed 
fresh_ingredient_id_ranges = np.delete(fresh_ingredient_id_ranges, id_ranges_to_delete, 0)

for id_range in fresh_ingredient_id_ranges:
    fresh_ingredient_ids_count += id_range[1] - id_range[0] + 1

print(f"The fresh ingredient ID ranges consider a total of {fresh_ingredient_ids_count} ingredient IDs to be fresh.")

raw_inputs.close()