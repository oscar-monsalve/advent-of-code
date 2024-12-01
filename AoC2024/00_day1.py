with open("test", "r") as file:

    left = []
    right = []

    for i in file:
        i = i.rsplit()
        left.append(int(i[0]))
        right.append(int(i[1]))
        left.sort()
        right.sort()

    # sum_diff = 0  # for part 1
    # for i, k in zip(left, right):  # for part 1
        # diff = abs(i - k)  # for part 1
        # sum_diff += diff  # for part 1

    for i in left:
        times_appeared = 0
        for k in right:
            if i == k:
                times_appeared += 1

    print(times_appeared)
