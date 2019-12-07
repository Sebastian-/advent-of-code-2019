total_fuel = 0

def required_fuel(mass):
  fuel = mass // 3 - 2
  
  if (fuel <= 0):
    return 0
  else:
    return fuel + required_fuel(fuel)

with open('data.txt') as masses:
  for mass in masses:
    total_fuel += required_fuel(int(mass))

print(total_fuel)





