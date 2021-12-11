from typing import List, Set
from utils import Point, get_input_lines

inp_lines = get_input_lines('11.txt')

# inp_lines = [
#     '11111',
#     '19991',
#     '19191',
#     '19991',
#     '11111'
# ]

plain = [[int(c) for c in line] for line in inp_lines]


def step1(plain: List[List]) -> List[List]:
    for y, row in enumerate(plain):
        for x, octopus in enumerate(row):
            plain[y][x] = octopus + 1

    return plain


def get_neighbours(plain, point: Point) -> List[Point]:
    neighbours = []
    if point.x > 0:
        neighbours.append(Point(point.x - 1, point.y))
        if point.y > 0:
            neighbours.append(Point(point.x - 1, point.y - 1))
        if point.y < len(plain) - 1:
            neighbours.append(Point(point.x - 1, point.y + 1))

    if point.y > 0:
        neighbours.append(Point(point.x, point.y - 1))
    if point.y < len(plain) - 1:
        neighbours.append(Point(point.x, point.y + 1))

    if point.x < len(plain[point.y]) - 1:
        neighbours.append(Point(point.x + 1, point.y))
        if point.y > 0:
            neighbours.append(Point(point.x + 1, point.y - 1))
        if point.y < len(plain) - 1:
            neighbours.append(Point(point.x + 1, point.y + 1))

    return neighbours


def flash_bfs(plain, point: Point, flashed: Set[Point]) -> None:
    q = [point]
    while len(q):
        p = q.pop(0)
        if p in flashed:
            continue
        neighbours = get_neighbours(plain, p)
        for n in neighbours:
            plain[n.y][n.x] += 1
            if plain[n.y][n.x] > 9 and n not in flashed:
                q.append(n)

        flashed.add(p)


def step2(plain: List[List]) -> Set[Point]:
    flashed: Set[Point] = set()
    for y in range(len(plain)):
        for x in range(len(plain[y])):
            p = Point(x, y)
            if plain[p.y][p.x] > 9 and p not in flashed:
                flash_bfs(plain, p, flashed)

    return flashed


def step3(plain, flashed):
    for p in flashed:
        plain[p.y][p.x] = 0


total_flashes: int = 0

for _ in range(100):
    step1(plain)
    flashed = step2(plain)
    step3(plain, flashed)
    total_flashes += len(flashed)

print(f'Answer 1: {total_flashes}')


step = 0
while True:
    step1(plain)
    flashed = step2(plain)
    step3(plain, flashed)
    step += 1

    if all(l == [0] * 10 for l in plain):
        print(f'Answert 2: {step + 100}')
        break
