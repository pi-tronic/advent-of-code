inputs = open("inputs.txt")

# extract the id ranges
id_ranges = [[int(id_range.split('-')[0]), int(id_range.split('-')[1])] for id_range in inputs.readline().split(',')]

sum_of_invalid_ids = 0

# cycle through each of the id ranges
for id_range in id_ranges:
    invalid_ids = []
    for id in range(id_range[0], id_range[1]+1):
        # INVALID IF
        # id consists of repeating pattern (at least two times)
        id_lenght = len(str(id))
        # need to find factors of id lenght
        factors = [factor for factor in range(2,id_lenght+1) if id_lenght % factor == 0]
        for factor in factors:
            # split id into factor parts of the same lenght
            id_parts = [int(str(id)[part*int(id_lenght/factor):part*int(id_lenght/factor)+int(id_lenght/factor)]) for part in range(factor)]
            # check, if all parts are equal
            if all(id_parts[0] == part for part in id_parts):
                invalid_ids.append(id)
                sum_of_invalid_ids += id
                break
    print(f"{id_range[0]}-{id_range[1]} has {len(invalid_ids)} invalid IDs: {invalid_ids}.")

print(f"Adding up all the invalid IDs produces {sum_of_invalid_ids}.")

inputs.close()