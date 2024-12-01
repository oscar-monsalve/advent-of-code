with open("input", "r") as file:

    left = []
    right = []

    for i in file:
        i = i.rsplit()
        left.append(int(i[0]))
        right.append(int(i[1]))
        left.sort()
        right.sort()

    sum_diff = 0
    for i, k in zip(left, right):
        diff = abs(i - k)
        sum_diff += diff

    print(sum_diff)
