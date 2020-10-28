with open("data02.txt") as datafile:
    data = datafile.read().replace("\n", "")

int_code = [int(i) for i in data.split(",")]

print(f"data list : {int_code}")


def read_intcode2(intcode, noun, verb):
    local_intcode = intcode.copy()
    local_intcode[1] = noun
    local_intcode[2] = verb
    counter = 0
    while True:
        opcode = local_intcode[counter]
        if opcode == 99:
            break
        first_pos = local_intcode[counter + 1]
        second_pos = local_intcode[counter + 2]
        third_pos = local_intcode[counter + 3]

        if opcode == 1:
            local_intcode[third_pos] = (
                local_intcode[first_pos] + local_intcode[second_pos]
            )
        elif opcode == 2:
            local_intcode[third_pos] = (
                local_intcode[first_pos] * local_intcode[second_pos]
            )
        else:
            raise IndexError(f"Opcode was neither 1, 2, nor 99. It was {opcode}")

        counter += 4

    return local_intcode[0]


test1_intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
test2 = [1, 0, 0, 0, 99]
test3 = [2, 3, 0, 3, 99]
test4 = [2, 4, 4, 5, 99, 0]
test5 = [1, 1, 1, 4, 99, 5, 6, 0, 99]


for a in range(100):
    for b in range(100):
        output = read_intcode2(int_code, a, b)
        if output == 19690720:
            print(f"Found the values. Noun: {a} Verb: {b}")
            print(f"100 * noun + verb = {100 * a + b}")
