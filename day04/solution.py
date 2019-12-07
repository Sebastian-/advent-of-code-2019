def hasRepeatAdjacent(num):
  prevDigit = ''

  for digit in str(num):
    if digit == prevDigit:
      return True
    prevDigit = digit
  
  return False


def isNotDecreasing(num):
  prevDigit = '0'

  for digit in str(num):
    if digit < prevDigit:
      return False
    prevDigit = digit
  
  return True


def hasIsolatedPair(num):
  prevDigit = str(num)[0]
  count = 1
  counts = []

  for digit in str(num)[1:]:
    if digit == prevDigit:
      count = count + 1
    else:
      counts.append(count)
      count = 1
    
    prevDigit = digit
  
  counts.append(count)
  
  if len(list(filter(lambda x: x == 2, counts))) > 0:
    return True
  
  return False


def main():
  result = 0
  passwords = []

  for i in range(246515,739106):
    if hasRepeatAdjacent(i) and isNotDecreasing(i):
      result = result + 1
      passwords.append(i)
  
  # Part 1
  print(len(passwords))

  # Part 2
  print(len(list(filter(lambda x: hasIsolatedPair(x), passwords))))


if __name__ == "__main__":
    main()