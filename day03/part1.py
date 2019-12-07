def plotPath(wirePath):
  visited = {(0, 0)}
  x = 0
  y = 0

  for step in wirePath:
    direction = step[0]
    distance = int(step[1:])

    if direction == 'U':
      for i in range(1, distance + 1):
        y = y + 1
        visited.add( (x, y) )
    elif direction == 'D':
      for i in range(1, distance + 1):
        y = y - 1
        visited.add( (x, y) )
    elif direction == 'L':
      for i in range(1, distance + 1):
        x = x - 1
        visited.add( (x, y) )
    elif direction == 'R':
      for i in range(1, distance + 1):
        x = x + 1
        visited.add( (x, y) )
  
  return visited


def minDist(intersections):
  distances = list(map(lambda x: abs(x[0]) + abs(x[1]), intersections))
  min_distance = 10000000000000000000
  for dist in distances:
    if abs(dist) < min_distance and dist != 0:
      min_distance = abs(dist)
  
  return min_distance

def main():
  with open('input.txt') as wires:
    wire1 = wires.readline().rstrip().split(',')
    wire2 = wires.readline().rstrip().split(',')

    w1_visited = plotPath(wire1)
    w2_visited = plotPath(wire2)

    print(minDist(w1_visited & w2_visited))

if __name__ == "__main__":
  main()