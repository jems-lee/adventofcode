#       A                      B                    C                  DE
# Third parameter mode, Second parameter mode, first parameter mode, Opcode


def read_data(filename="data05.txt"):
    with open(filename) as datafile:
        data = datafile.read().replace("\n", "")
    int_code = [int(i) for i in data.split(",")]
    return int_code


def read_intcode2(intcode, noun=None, verb=None):
    def interpret_param(param, param_num):
        if param == 0 and param_num != 3:
            pos1 = local_intcode[counter + param_num]
            value = local_intcode[pos1]
        else:
            value = local_intcode[counter + param_num]
        return value

    def interpret_opcode(opcode, param1, param2, param3):
        value1 = interpret_param(param1, 1)
        value2 = interpret_param(param2, 2)
        value3 = interpret_param(param3, 3)

        if opcode == 1:
            # print(f"value1: {value1} value2: {value2} value3: {value3}")
            local_intcode[value3] = value1 + value2
        elif opcode == 2:
            local_intcode[value3] = value1 * value2
        return None

    local_intcode = intcode.copy()
    local_intcode[1] = noun if noun else local_intcode[1]
    local_intcode[2] = verb if noun else local_intcode[2]
    counter = 0
    command = 0
    param1, param2, param3 = 0, 0, 0
    while True:
        previous_command = command
        previous_params = [param3, param2, param1]
        command = local_intcode[counter]
        opcode = command % 100
        param1 = (command % 1000) // 100
        param2 = (command % 10000) // 1000
        param3 = (command % 100000) // 10000

        if opcode == 99:
            break

        if opcode == 4:  # output
            output_pos = local_intcode[counter + 1]
            output_value = local_intcode[output_pos]
            counter += 2
            if output_value == 0:
                print(f"Test passed: {output_value}")
                # print(f"Previous command: {previous_command},{previous_params}")
            else:
                print(f"Test failed: output: {output_value}")
                print(f"Previous command: {previous_command},{previous_params}")

        elif opcode == 3:
            input_value = 1
            input_position = local_intcode[counter + 1]
            local_intcode[input_position] = input_value
            counter += 2

        elif opcode == 1 or opcode == 2:
            interpret_opcode(opcode, param1, param2, param3)
            counter += 4
        else:
            raise IndexError(f"Opcode was neither 1, 2, nor 99. It was {opcode}")

    return local_intcode


def main():
    int_code = read_data()
    # print(f"data list : {int_code}")
    test1_intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    test2 = [1, 0, 0, 0, 99]
    test3 = [2, 3, 0, 3, 99]
    test4 = [2, 4, 4, 5, 99, 0]
    test5 = [1, 1, 1, 4, 99, 5, 6, 0, 99]

    test6 = [1002, 4, 3, 4, 33]
    test7 = [102, 8, 223, 223]

    final_intcode = read_intcode2(int_code)
    print(final_intcode)
    # 4511442


if __name__ == "__main__":
    main()
