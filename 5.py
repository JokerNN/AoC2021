from utils import get_input_lines
from collections import namedtuple, defaultdict

Point = namedtuple('Point', ['x', 'y'], defaults=(0, 0))

input = get_input_lines('5.txt')

plain = defaultdict(int)

for line in input:
    p1_str, p2_str = line.split(' -> ')
    p1 = Point(*(int(n) for n in p1_str.split(',')))
    p2 = Point(*(int(n) for n in p2_str.split(',')))

    if p1.x != p2.x and p1.y != p2.y:
        continue

    if p1.x == p2.x:
        fp, tp = sorted([p1, p2])
        for y in range(fp.y, tp.y + 1):
            plain[Point(p1.x, y)] += 1
    else:
        fp, tp = sorted([p1, p2])
        for x in range(fp.x, tp.x + 1):
            plain[Point(x, fp.y)] += 1

c = sum(1 if v > 1 else 0 for v in plain.values())
print(f'Answer 1: {c}')

plain = defaultdict(int)


for line in input:
    p1_str, p2_str = line.split(' -> ')
    p1 = Point(*(int(n) for n in p1_str.split(',')))
    p2 = Point(*(int(n) for n in p2_str.split(',')))
    dx, dy = p1.x - p2.x, p1.y - p2.y
    vec = Point(0, 0)
    if dx != 0 and dy != 0:
        vec = Point(abs(dx) // dx, abs(dy) // dy)
    elif dx == 0:
        vec = Point(0, abs(dy) // dy)
    elif dy == 0:
        vec = Point(abs(dx) // dx, 0)

    while True:
        plain[p2] += 1
        p2 = Point(p2.x + vec.x, p2.y + vec.y)
        if p1 == p2:
            plain[p2] += 1
            break


c = sum(1 if v > 1 else 0 for v in plain.values())
print(f'Answer 2: {c}')
