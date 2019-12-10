from fractions import Fraction


def count_detections(grid):
    # key - coordinates of an asteroid
    # value - set of coordinates viewable from that asteroid
    viewable = {}
    width = len(grid[0])
    height = len(grid)

    # init viewable
    for x in range(width):
        for y in range(height):
            viewable[(x, y)] = set()

    for x in range(width):
        for y in range(height):
            if grid[y][x] == '.':
                continue

            # Quadrant I and II
            obscured_slopes = set()
            for dx in range(-x, width-x):
                for dy in range(-1, -y-1, -1):
                    if grid[y+dy][x+dx] == '.' or dx == 0 or Fraction(dy, dx) in obscured_slopes:
                        continue
                    obscured_slopes.add(Fraction(dy, dx))
                    viewable[(x, y)].add((x+dx, y+dy))

            # Quadrant III and IV
            obscured_slopes = set()
            for dx in range(-x, width-x):
                for dy in range(1, height-y):
                    if grid[y+dy][x+dx] == '.' or dx == 0 or Fraction(dy, dx) in obscured_slopes:
                        continue
                    obscured_slopes.add(Fraction(dy, dx))
                    viewable[(x, y)].add((x+dx, y+dy))

            # Check vertical
            for dy in range(-1, -y-1, -1):
                if grid[y+dy][x] == '#':
                    viewable[(x, y)].add((x, y+dy))
                    break

            for dy in range(1, height-y):
                if grid[y+dy][x] == '#':
                    viewable[(x, y)].add((x, y+dy))
                    break

            # Check horizontal
            for dx in range(-1, -x-1, -1):
                if grid[y][x+dx] == '#':
                    viewable[(x, y)].add((x+dx, y))
                    break

            for dx in range(1, width-x):
                if grid[y][x+dx] == '#':
                    viewable[(x, y)].add((x+dx, y))
                    break

    # view_map = []
    # for y in range(height):
    #     row = []
    #     for x in range(width):
    #         if grid[y][x] == '#':
    #             row.append(len(viewable[(x, y)]))
    #         else:
    #             row.append('.')
    #     view_map.append(row)

    # for row in view_map:
    #     print(''.join([str(x) for x in row]))

    return viewable


def main():
    grid = []

    with open('input.txt') as field:
        for row in field:
            grid.append(list(row.strip()))

    # print([{key: len(val)} if len(val) != 0 else '' for key,
    #        val in count_detections(grid).items()])

    max_observable = 0
    point = None
    for key, val in count_detections(grid).items():
        if len(val) > max_observable:
            max_observable = len(val)
            point = key

    print(f'{max_observable} asteroids seen from {point}')


if __name__ == "__main__":
    main()
