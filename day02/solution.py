def execute(program, op_index):
  for i in range(0, len(program), 4):
    op_code = program[i]

    if op_code == 99:
      return program
    
    op1_address = program[i+1]
    op2_address = program[i+2]
    dest = program[i+3]

    if op_code == 1:
      program[dest] = program[op1_address] + program[op2_address]
    
    if op_code == 2:
      program[dest] = program[op1_address] * program[op2_address]



def run():
  with open('data.txt') as program_file:
    program = program_file.read().split(',')
    program = list(map(lambda x: int(x), program))
    for i in range(0, 99):
      for j in range(0, 99):
        current_program = program.copy()
        current_program[1] = i
        current_program[2] = j
        if execute(current_program, 0)[0] == 19690720:
          print(f'noun: {i}, verb: {j}')


if __name__ == "__main__":
  run()