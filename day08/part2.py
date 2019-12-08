def main():
  with open('input.txt') as i:
    data = str(i.readline())
    layers = []

    while data:
      layer = []
      
      for i in range(6):
        row = [int(d) for d in data[:25]]
        layer.append(row)
        data = data[25:]

      layers.append(layer)

    img = layers[0]
    for layer in layers[1:]:
      for i, row in enumerate(layer):
        for j, pixel in enumerate(row):
          if (pixel == 1 or pixel == 0) and img[i][j] == 2:
            img[i][j] = pixel
    
    for row in img:
      print(''.join(['X' if d == 1 else " " for d in row]))
    

if __name__ == "__main__":
    main()