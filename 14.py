from typing import Optional, Dict
from utils import get_input_lines
from collections import Counter
from copy import deepcopy


inp = get_input_lines('14.txt')

pattern = inp[0]


transformations = {}
for line in inp[2:]:
    f, to = line.split(' -> ')
    transformations[f] = to

polymer = Counter()

for idx in range(1, len(pattern)):
    pair = pattern[idx - 1] + pattern[idx]
    polymer[pair] += 1


def transform(polymer: Counter, transformations: Dict[str, str]) -> Dict[str, str]:
    new_poly = deepcopy(polymer)
    for k in list(polymer.keys()):
        if k in transformations:
            nk1 = k[0] + transformations[k]
            nk2 = transformations[k] + k[1]
            new_poly[nk1] += polymer[k]
            new_poly[nk2] += polymer[k]
            new_poly[k] -= polymer[k]

    return new_poly


for _ in range(10):
    polymer = transform(polymer, transformations)


counts = Counter()
for pair, count in polymer.items():
    if count > 0:
        counts[pair[0]] += count

counts[pattern[-1]] += 1

ans1 = counts.most_common()[0][1] - counts.most_common()[-1][1]

print(f'Answer 1: {ans1}')

for _ in range(30):
    polymer = transform(polymer, transformations)


counts = Counter()
for pair, count in polymer.items():
    if count > 0:
        counts[pair[0]] += count

counts[pattern[-1]] += 1

ans2 = counts.most_common()[0][1] - counts.most_common()[-1][1]

print(f'Answer 1: {ans2}')
