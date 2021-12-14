from copy import copy
from typing import DefaultDict
from utils import get_input_lines, Point
inp = get_input_lines('13.txt')

PaperType = DefaultDict[Point, bool]


def fold_horizontally(paper: PaperType, y: int, bottom_left: Point):
    cur_y = y + 1
    while cur_y <= bottom_left.y:
        for cur_x in range(bottom_left.x + 1):
            top = Point(cur_x, 2 * y - cur_y)
            bottom = Point(cur_x, cur_y)
            paper[top] = paper[bottom] or paper[top]

        cur_y += 1

    for point in list(paper.keys()):
        if point.y > y:
            del paper[point]


def fold_vertically(paper: PaperType, x: int, bottom_left: Point):
    cur_x = x + 1
    while cur_x <= bottom_left.x:
        for cur_y in range(bottom_left.y + 1):
            left = Point(2 * x - cur_x, cur_y)
            right = Point(cur_x, cur_y)
            paper[left] = paper[left] or paper[right]

        cur_x += 1

    for point in list(paper.keys()):
        if point.x > x:
            del paper[point]


dots = []
folds = []
for line in inp:
    if line == '':
        continue
    if line.startswith('fold along'):
        fold = line.replace('fold along ', '').split('=')
        fold[1] = int(fold[1])
        folds.append(fold)
    else:
        dots.append(Point(*(int(i) for i in line.split(','))))


paper: PaperType = DefaultDict(bool)
mx, my = -float('inf'), -float('inf')
for dot in dots:
    paper[dot] = True
    mx = max(mx, dot.x)
    my = max(my, dot.y)

fold = folds[0]
bottom_left = Point(mx, my)

if fold[0] == 'x':
    fold_vertically(paper, fold[1], bottom_left)
    bottom_left = Point(fold[1], bottom_left.y)
elif fold[0] == 'y':
    fold_horizontally(paper, fold[1], bottom_left)
    bottom_left = Point(bottom_left.x, fold[1])


ans1 = sum(1 if v else 0 for v in paper.values())
print(f'Answer 1: {ans1}')


for fold in folds[1:]:
    if fold[0] == 'x':
        fold_vertically(paper, fold[1], bottom_left)
        bottom_left = Point(fold[1], bottom_left.y)
    elif fold[0] == 'y':
        fold_horizontally(paper, fold[1], bottom_left)
        bottom_left = Point(bottom_left.x, fold[1])

screen = [['.'] * bottom_left.x for _ in range(bottom_left.y)]
print(screen)

for point, val in paper.items():
    if val:
        screen[point.y][point.x] = '#'

print('\n'.join(''.join(line) for line in screen))
