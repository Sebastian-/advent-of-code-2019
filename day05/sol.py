def getOpCode(i):
  return int(str(i)[-2:])


def getParaModes(i):
  modes = list(map(lambda x: int(x), str(i)[:-2]))
  
  while len(modes) < 2:
    modes.insert(0,0)
  
  return modes


def getOperand(program, addr, mode):
  operand = None
  try:
    operand = program[addr] if mode == 1 else program[program[addr]]
  except IndexError:
    pass
  return operand


def execute(program):
  pc = 0

  while True:
    op_code = getOpCode(program[pc])
    modes = getParaModes(program[pc])

    op1 = getOperand(program, pc + 1, modes[-1])
    op2 = getOperand(program, pc + 2, modes[-2])

    if op_code == 99:
      return

    # Add
    if op_code == 1:
      program[program[pc + 3]] = op1 + op2
      pc += 4
      continue
    
    # Multiply
    if op_code == 2:
      program[program[pc + 3]] = op1 * op2
      pc += 4
      continue
    
    # Input
    if op_code == 3:
      x = input('Input a single integer: ')
      program[program[pc + 1]] = int(x)
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
      program[program[pc + 3]] = 1 if op1 < op2 else 0
      pc += 4
      continue
    
    # Equals
    if op_code == 8:
      program[program[pc + 3]] = 1 if op1 == op2 else 0
      pc += 4
      continue


def main():
  with open('input.txt') as program_file:
    program = program_file.read().split(',')
    program = list(map(lambda x: int(x), program))
    execute(program)

if __name__ == "__main__":
  main()
