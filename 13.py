from copy import copy
from typing import DefaultDict, Dict
from utils import get_input_lines, Point
inp = get_input_lines('13.txt')

PaperType = Dict[Point, bool]


def fold_horizontally(paper: PaperType, y: int):
    for point in list(paper.keys()):
        if point.y > y:
            reflection = Point(point.x, 2 * y - point.y)
            paper[reflection] = True
            del paper[point]


def fold_vertically(paper: PaperType, x: int):
    for point in list(paper.keys()):
        if point.x > x:
            reflection = Point(2 * x - point.x, point.y)
            paper[reflection] = True
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


paper: PaperType = {}

for dot in dots:
    paper[dot] = True

fold = folds[0]

if fold[0] == 'x':
    fold_vertically(paper, fold[1])
elif fold[0] == 'y':
    fold_horizontally(paper, fold[1])


ans1 = sum(1 if v else 0 for v in paper.values())
print(f'Answer 1: {ans1}')


for fold in folds[1:]:
    if fold[0] == 'x':
        fold_vertically(paper, fold[1])
    elif fold[0] == 'y':
        fold_horizontally(paper, fold[1])


blx = max(paper.keys(), key=lambda p: p.x)
bly = max(paper.keys(), key=lambda p: p.y)

screen = [['.'] * (blx.x + 1) for _ in range(bly.y + 1)]

for point, val in paper.items():
    if val:
        screen[point.y][point.x] = '#'
print('Answer 2:')
print('\n'.join(''.join(line) for line in screen))
