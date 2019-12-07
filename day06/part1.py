def count_orbits(orbit_map):
  queue = ['COM']
  distance = 0
  orbit_count = 0

  while queue:
    next_queue = []

    for planet in queue:
      orbit_count += distance

      if planet in orbit_map:
        next_queue.extend(orbit_map[planet])
    
    distance += 1
    queue = next_queue
  
  return orbit_count
  

def main():
  tree = {}

  with open('input.txt') as orbit_data:

    for orbit in orbit_data:
      center = orbit.split(')')[0]
      orbiter = orbit.split(')')[1].rstrip()

      if center in tree.keys():
        tree[center].append(orbiter)
      else:
        tree[center] = [orbiter]
  
  print (count_orbits(tree))


if __name__ == "__main__":
    main()