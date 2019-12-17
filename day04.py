# 172851-675869
# two adjacent digits are the same
# going from left to right, the number does not decrease

# 177777

# Find all possible non decreasing numbers

def get_increasing_numbers(first, last):
    numbers_list = list()
    for i1 in range(10):
        for i2 in range(i1, 10):
            for i3 in range(i2, 10):
                for i4 in range(i3, 10):
                    for i5 in range(i4, 10):
                        for i6 in range(i5, 10):
                            number = 100000 * i1 + 10000 * i2 + 1000 * i3 + 100 * i4 + 10 * i5 + i6
                            if first <= number <= last and (
                                    (i1 == i2 and i1 != i3) or
                                    (i2 == i3 and i2 != i1 and i2 != i4) or
                                    (i3 == i4 and i3 != i2 and i3 != i5) or
                                    (i4 == i5 and i4 != i3 and i4 != i6) or
                                    (i5 == i6 and i5 != i4)
                            ):
                                numbers_list.append(number)
    return numbers_list


increasing_numbers = get_increasing_numbers(172851, 675869)
print(len(increasing_numbers))

# 1260
# 1135 correct
