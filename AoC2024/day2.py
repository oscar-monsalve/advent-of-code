data_strings = []
reports = []

with open("day2.input", "r") as file:
    for i in file:
        i = i.rstrip().split(" ")
        data_strings.append(i)

# reports = [list(map(int, sublist)) for sublist in data_strings]  # does the same this as the for loop.
for sublist in data_strings:
    inner_list = []
    for string in sublist:
        inner_list.append(int(string))
    reports.append(inner_list)


# part 1
def is_decreasing(row: list):
    return all(row[i] > row[i + 1] for i in range(len(row) - 1))


def is_increasing(row: list):
    return all(row[i] < row[i + 1] for i in range(len(row) - 1))


def allowed_distance(row: list):
    return all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1))


# part 2
def remove_bad_level(row: list) -> list:
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row.pop(i)
            return row
        # if not (1 <= abs(row[i] - row[i + 1]) <= 3):
        #     row.pop(i + 1)
        #     return row

    for i in range(len(row) - 2):
        if row[i] < row[i + 1] > row[i + 2] or row[i] > row[i + 1] < row[i + 2]:
            row.pop(i + 1)
            return row

        left_diff = abs(row[i] - row[i + 1])
        right_diff = abs(row[i + 1] - row[i + 2])
        if left_diff > 3 and left_diff > right_diff:
            row.pop(i)
            return row
        if left_diff > 3 and left_diff < right_diff:
            row.pop(i + 2)
            return row
        if right_diff > 3 and right_diff > left_diff:
            row.pop(i + 2)
            return row
        if right_diff > 3 and right_diff < left_diff:
            row.pop(i)
            return row
    return row


# test_reports = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]
# for index, lists in enumerate(test_reports):
#     new_list = remove_bad_level(lists)
#     print(new_list)


safe_reports = 0
for index, report_list in enumerate(reports):
    new_list = remove_bad_level(report_list)
    print(new_list)
    if is_decreasing(new_list):
        if allowed_distance(new_list):
            # print(f"Report {index}: safe")
            safe_reports += 1
    if is_increasing(new_list):
        if allowed_distance(new_list):
            # print(f"Report {index}: safe")
            safe_reports += 1
print(safe_reports)
