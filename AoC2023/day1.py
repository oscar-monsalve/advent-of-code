with open("example_1.txt") as input:

    sum = 0
    numbers = {
            "one":   1,
            "two":   2,
            "three": 3,
            "four":  4,
            "five":  5,
            "six":   6,
            "seven": 7,
            "eight": 8,
            "nine":  9
        }
    for i in input:
        digits = []
        letters = []
        letter_sum = ""
        words = []
        i = i.rstrip()
        for ii in i:
            if ii.isnumeric():
                digits.append(ii)
            elif ii.isalpha():
                letter_sum += ii
        
        for i in letter_sum:
            if i in numbers.keys():
                words.append(i)
                    
        # calibration = int(digits[0] + digits[-1])
        # sum += calibration
        
        print(digits)
        print(letter_sum)
        print(words)
