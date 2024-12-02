data_strings = []
reports = []

with open("day2.test", "r") as file:
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
# print(reports)

for i in reports:
    for index, number in enumerate(i):
        count = 0
        while count < len(i):
            print(number)
            count += 1
