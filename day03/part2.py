def plotPath(wirePath):
  visited = {}
  x = 0
  y = 0
  numSteps = 0

  for step in wirePath:
    direction = step[0]
    distance = int(step[1:])

    if direction == 'U':
      for i in range(1, distance + 1):
        y = y + 1
        numSteps = numSteps + 1
        visited.setdefault((x, y), []).append(numSteps)
    elif direction == 'D':
      for i in range(1, distance + 1):
        y = y - 1
        numSteps = numSteps + 1
        visited.setdefault((x, y), []).append(numSteps)
    elif direction == 'L':
      for i in range(1, distance + 1):
        x = x - 1
        numSteps = numSteps + 1
        visited.setdefault((x, y), []).append(numSteps)
    elif direction == 'R':
      for i in range(1, distance + 1):
        x = x + 1
        numSteps = numSteps + 1
        visited.setdefault((x, y), []).append(numSteps)
  
  return visited


def minDist(intersections):
  distances = list(map(lambda x: abs(x[0]) + abs(x[1]), intersections))
  min_distance = float('inf')
  for dist in distances:
    if abs(dist) < min_distance and dist != 0:
      min_distance = abs(dist)
  
  return min_distance


def minSteps(intersections, w1_path, w2_path):
  min_steps = float('inf')
  for i in intersections:
    if not (i[0] == 0 and i[1] == 0):
      total_steps = min(w1_path[i]) + min(w2_path[i])
      if total_steps < min_steps:
        min_steps = total_steps
  
  return min_steps


def main():
  with open('input.txt') as wires:
    wire1 = wires.readline().rstrip().split(',')
    wire2 = wires.readline().rstrip().split(',')

    w1_path = plotPath(wire1)
    w2_path = plotPath(wire2)
    intersections = w1_path.keys() & w2_path.keys()

    print(minDist(intersections))
    print(minSteps(intersections, w1_path, w2_path))

if __name__ == "__main__":
  main()