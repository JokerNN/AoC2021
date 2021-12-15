from typing import Set, List
from utils import get_input_lines, Point
import heapq

inp = get_input_lines('15.txt')
cave_map = []

for line in inp:
    row = []
    for c in line:
        row.append(int(c))
    cave_map.append(row)


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


def dijkstra(cave_map, source: Point):
    dist = {}
    prev = {}
    Q: Set[Point] = set()
    for y in range(len(cave_map)):
        for x in range(len(cave_map[y])):
            p = Point(x, y)
            dist[p] = float('inf')
            prev[p] = None
            Q.add(p)

    dist[source] = 0

    while Q:
        point = min(Q, key=lambda p: dist[p])
        Q.remove(point)

        for neighbour in get_neighbour_points(cave_map, point):
            if neighbour not in Q:
                continue

            alt = dist[point] + cave_map[point.y][point.x]
            if alt < dist[neighbour]:
                dist[neighbour] = alt
                prev[neighbour] = point

    return dist, prev


d = dijkstra(cave_map, Point(0, 0))
ans1 = d[0][Point(len(cave_map[0]) - 1, len(cave_map) - 1)]

print(f'Answer 1: {ans1}')

p = Point(99, 99)
while p:
    next_p = d[1][p]
    if not next_p:
        break
    if next_p.x > p.x or next_p.y > p.y:
        print("ALERT", p, next_p)
    p = next_p
