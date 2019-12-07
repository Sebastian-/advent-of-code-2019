import itertools

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


def execute(program, inputs, pc_start):
  pc = pc_start

  while True:
    op_code = getOpCode(program[pc])
    modes = getParaModes(program[pc])

    op1 = getOperand(program, pc + 1, modes[-1])
    op2 = getOperand(program, pc + 2, modes[-2])

    if op_code == 99:
      return -1,-1

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
      #x = input('Input a single integer: ')
      x = inputs.pop(0)
      program[program[pc + 1]] = int(x)
      pc += 2
      continue
    
    # Output
    if op_code == 4:
      # print(op1)
      # pc += 2
      # continue
      return (op1, pc+2)
    
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


def execute_feedback_loop(program, inputs):
  signal = 0
  amp_programs = []
  amp_pc = []

  for i in inputs:
    p = program.copy()
    signal, pc = execute(p, [i, signal], 0)
    amp_programs.append(p)
    amp_pc.append(pc)

  while True:
    for i in range(5):
      thrust, pc = execute(amp_programs[i], [signal, signal], amp_pc[i])
      amp_pc[i] = pc
      signal = thrust if pc != -1 else signal
      if i == 4 and pc == -1:
        return signal

  return signal

def main():
  with open('input.txt') as program_file:
    program = program_file.read().split(',')
    program = list(map(lambda x: int(x), program))

    max_thrust = 0

    for perm in itertools.permutations([5,6,7,8,9]):
      thrust = execute_feedback_loop(program, list(perm))
      max_thrust = max(max_thrust, thrust)
    
    print(max_thrust)




if __name__ == "__main__":
  main()
