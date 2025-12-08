input = []
with open("02_input.txt", "r") as file:
    for i in file:
        i = i.strip().split(",")
        for id_str in i:
            id_str = id_str.split("-")
            input.append([int(x) for x in id_str])

# Part 1 function
def split_number_digits(number: int) -> list[int]:
    s = str(number)
    mid_index = len(s) // 2
    part1 = s[:mid_index]
    part2 = s[mid_index:]
    return int(part1), int(part2)


invalid_ids = []
for _, current in enumerate(input):
    for ranges in range(current[0], current[1] + 1):
        if len(str(ranges)) % 2 != 0:
            # print("Valid ID.")
            pass
        elif len(str(ranges)) % 2 == 0:
            num1, num2 = split_number_digits(ranges)
            if num1 == num2:
                invalid_id = int(str(num1) + str(num2))
                # print(f"{invalid_id} Invalid ID")
                invalid_ids.append(invalid_id)

sum_invalid_ids = sum(invalid_ids)

# print(invalid_ids)
print(f"Sum of invalid IDs: {sum_invalid_ids}")
