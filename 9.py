from typing import List, NamedTuple, Set
from collections import namedtuple
from utils import get_input_lines

Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])

inp = get_input_lines('9.txt')
map = [list(line) for line in inp]


def get_neighbours(map, x, y):
    neighbours = []
    if x > 0:
        neighbours.append(map[y][x - 1])

    if x < len(map[y]) - 1:
        neighbours.append(map[y][x + 1])

    if y > 0:
        neighbours.append(map[y - 1][x])

    if y < len(map) - 1:
        neighbours.append(map[y + 1][x])

    return neighbours


def get_neighbour_points(map, point) -> List[Point]:
    neighbours = []
    x, y = point
    if x > 0:
        neighbours.append(Point(x - 1, y))

    if x < len(map[y]) - 1:
        neighbours.append(Point(x + 1, y))

    if y > 0:
        neighbours.append(Point(x, y - 1))

    if y < len(map) - 1:
        neighbours.append(Point(x, y + 1))

    return neighbours


risks = []
for x in range(len(map[0])):
    for y in range(len(map)):
        neighbours = get_neighbours(map, x, y)
        point = map[y][x]
        if all(n > point for n in neighbours):
            risks.append(int(point))

res = sum(risks) + len(risks)

print(f"Answer 1: {res}")


def bfs(map, point: Point) -> Set[Point]:
    q = [point]
    visited = set()
    while len(q):
        point = q.pop(0)
        if point in visited:
            continue
        neighbours = get_neighbour_points(map, point)

        for neighbour in neighbours:
            x, y = neighbour
            if map[y][x] == '9' or neighbour in visited:
                continue
            else:
                q.append(neighbour)

        visited.add(point)

    return visited


global_visited = set()
baisins = []
for y, row in enumerate(map):
    for x, depth in enumerate(row):
        point = Point(x, y)
        if depth != '9' and point not in global_visited:
            baisin = bfs(map, point)
            global_visited |= baisin
            baisins.append(baisin)

        # import sys
        # sys.exit(0)

sizes = sorted([len(b) for b in baisins], reverse=True)
print(f'Answer 2: {sizes[0] * sizes[1] * sizes[2]}')
