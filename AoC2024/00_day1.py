with open("input", "r") as file:

    left = []
    right = []

    for i in file:
        i = i.rsplit()
        left.append(int(i[0]))
        right.append(int(i[1]))
        left.sort()
        right.sort()

    sum_diff = 0  # for part 1
    similarity_num = 0  # for part 2

    for i, k in zip(left, right):  # for part 1
        diff = abs(i - k)  # for part 1
        sum_diff += diff  # for part 1
        for j in right:  # for part 2
            if i == j:
                similarity_num += j

    print(f"part 1 answer: {sum_diff}")
    print(f"part 2 answer: {similarity_num}")
