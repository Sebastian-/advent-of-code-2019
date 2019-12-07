def count_transfers(children, parents):
  queue = ['SAN']
  distance = 0
  visited = set()

  while queue:
    next_queue = []

    for planet in queue:
      if planet == 'YOU':
        return distance
      
      if planet in visited:
        continue

      visited.add(planet)

      if planet in children:
        next_queue.extend(children[planet])
      
      if planet in parents:
        next_queue.extend(parents[planet])
    
    distance += 1
    queue = next_queue
  

def main():
  children = {}
  parents = {}

  with open('test1.txt') as orbit_data:

    for orbit in orbit_data:
      center = orbit.split(')')[0]
      orbiter = orbit.split(')')[1].rstrip()

      if center in children:
        children[center].append(orbiter)
      else:
        children[center] = [orbiter]

      if orbiter in parents:
        parents[orbiter].append(center)
      else:
        parents[orbiter] = [center]
  
  print (count_transfers(children, parents))


if __name__ == "__main__":
    main()