# Implemented sign function for part 2. Didn't want to use numpy
def sign(x: float) -> int:
    return (x > 0) - (x < 0)


instructions = []
with open("01_input.txt", "r") as file:
    for i in file:
        i = i.split()
        for data in i:
            instructions.append(int(data.replace("L", "-").replace("R", "")))

current_dial = 50
count_dial_points_zero = 0
dial_results = []

for i in instructions:
    for j in range(1, abs(i) + 1):
        current_dial = (current_dial + (1 * sign(i))) % 100
        if j == abs(i):
            dial_results.append(current_dial)
        if current_dial == 0:
            count_dial_points_zero += 1

# print(dial_results)
print(f"Number of dials at zero: {count_dial_points_zero}")
