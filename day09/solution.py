def get_op_code(i):
    return int(str(i)[-2:])


def get_paramater_modes(i):
    modes = list(map(lambda x: int(x), str(i)[:-2]))

    while len(modes) < 3:
        modes.insert(0, 0)

    return modes


def get_op_len(op_code):
    lengths = {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 2
    }
    return lengths[op_code]


def resolve_address(program, base, addr, mode):
    if mode == 2:
        return base + program[addr]
    elif mode == 1:
        return addr
    elif mode == 0:
        return program[addr]


def get_operand(program, base, addr, mode):
    operand = None

    try:
        operand = program[resolve_address(program, base, addr, mode)]
    except IndexError:
        pass

    return operand


def execute(program):
    pc = 0
    relative_base = 0
    memory = [0 for _ in range(len(program) * 200)]
    program += memory

    while True:
        op_code = get_op_code(program[pc])
        modes = get_paramater_modes(program[pc])

        op1 = get_operand(program, relative_base, pc+1, modes[-1])
        op2 = get_operand(program, relative_base, pc+2, modes[-2])
        dest = resolve_address(program, relative_base, pc+3, modes[-3])

        if op_code == 99:
            return

        # Add
        if op_code == 1:
            program[dest] = op1 + op2

        # Multiply
        if op_code == 2:
            program[dest] = op1 * op2

        # Input
        if op_code == 3:
            x = input('$: ')
            dest = resolve_address(program, relative_base, pc+1, modes[-1])
            program[dest] = int(x)

        # Output
        if op_code == 4:
            print(op1)

        # Jump if true
        if op_code == 5:
            if op1 != 0:
                pc = op2
                continue

        # Jump if false
        if op_code == 6:
            if op1 == 0:
                pc = op2
                continue

        # Less than
        if op_code == 7:
            program[dest] = 1 if op1 < op2 else 0

        # Equals
        if op_code == 8:
            program[dest] = 1 if op1 == op2 else 0

        # Shift relative base
        if op_code == 9:
            relative_base += op1

        pc += get_op_len(op_code)


def main():
    with open('input.txt') as program_file:
        program = program_file.read().split(',')
        program = list(map(lambda x: int(x), program))

        execute(program)


if __name__ == "__main__":
    main()
