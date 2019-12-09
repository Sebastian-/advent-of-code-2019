def getOpCode(i):
    return int(str(i)[-2:])


def getParaModes(i):
    modes = list(map(lambda x: int(x), str(i)[:-2]))

    while len(modes) < 3:
        modes.insert(0, 0)

    return modes


def resolveAddress(program, base, addr, mode):
    if mode == 2:
        return base + program[addr]
    elif mode == 1:
        return addr
    elif mode == 0:
        return program[addr]


def getOperand(program, base, addr, mode):
    operand = None

    try:
        operand = program[resolveAddress(program, base, addr, mode)]
    except IndexError:
        pass

    return operand


def execute(program):
    pc = 0
    relative_base = 0
    memory = [0 for _ in range(len(program) * 200)]
    program += memory

    while True:
        op_code = getOpCode(program[pc])
        modes = getParaModes(program[pc])

        op1 = getOperand(program, relative_base, pc+1, modes[-1])
        op2 = getOperand(program, relative_base, pc+2, modes[-2])
        dest = resolveAddress(program, relative_base, pc+3, modes[-3])

        if op_code == 99:
            return

        # Add
        if op_code == 1:
            program[dest] = op1 + op2
            pc += 4
            continue

        # Multiply
        if op_code == 2:
            program[dest] = op1 * op2
            pc += 4
            continue

        # Input
        if op_code == 3:
            x = input('$: ')
            dest = resolveAddress(program, relative_base, pc+1, modes[-1])
            program[dest] = int(x)
            pc += 2
            continue

        # Output
        if op_code == 4:
            print(op1)
            pc += 2
            continue

        # Jump if true
        if op_code == 5:
            if op1 != 0:
                pc = op2
            else:
                pc += 3
            continue

        # Jump if false
        if op_code == 6:
            if op1 == 0:
                pc = op2
            else:
                pc += 3
            continue

        # Less than
        if op_code == 7:
            program[dest] = 1 if op1 < op2 else 0
            pc += 4
            continue

        # Equals
        if op_code == 8:
            program[dest] = 1 if op1 == op2 else 0
            pc += 4
            continue

        # Relative base
        if op_code == 9:
            relative_base += op1
            pc += 2
            continue


def main():
    with open('input.txt') as program_file:
        program = program_file.read().split(',')
        program = list(map(lambda x: int(x), program))

        execute(program)


if __name__ == "__main__":
    main()
