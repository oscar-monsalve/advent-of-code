input = []
with open("02_input.txt", "r") as file:
    for i in file:
        i = i.strip().split(",")
        for id in i:
            input.append(id)

print(input)
