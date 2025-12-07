inputs = open("inputs.txt")

# extract the id ranges
id_ranges = [[int(id_range.split('-')[0]), int(id_range.split('-')[1])] for id_range in inputs.readline().split(',')]

sum_of_invalid_ids = 0

# cycle through each of the id ranges
for id_range in id_ranges:
    invalid_ids = []
    for id in range(id_range[0], id_range[1]+1):
        # INVALID IF
        # first half of id equals second half (so only for even digit counts)
        if len(str(id)) % 2 == 0:
            if str(id)[:int(len(str(id))/2)] == str(id)[int(len(str(id))/2):]:
                invalid_ids.append(id)
                sum_of_invalid_ids += id
    print(f"{id_range[0]}-{id_range[1]} has {len(invalid_ids)} invalid IDs: {invalid_ids}.")

print(f"Adding up all the invalid IDs produces {sum_of_invalid_ids}.")

inputs.close()