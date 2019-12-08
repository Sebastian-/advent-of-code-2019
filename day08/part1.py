def solve(layer):
  num_ones = 0
  num_twos = 0

  for row in layer:
    for i in row:
      if i == 1:
        num_ones += 1
      if i == 2:
        num_twos += 1
  
  return num_ones * num_twos


def count_zeros(layer):
  zeros = 0

  for row in layer:
    for i in row:
      if i == 0:
        zeros += 1
  
  return zeros


def main():
  with open('input.txt') as i:
    data = str(i.readline())
    layers = []

    min_zeros = float("inf")
    min_layer = []
    while data:
      layer = []
      
      for i in range(6):
        row = [int(d) for d in data[:25]]
        layer.append(row)
        data = data[25:]

      layers.append(layer)

      if count_zeros(layer) < min_zeros:
        min_layer = layer
        min_zeros = count_zeros(layer)
    
    print(solve(min_layer))
    

if __name__ == "__main__":
    main()