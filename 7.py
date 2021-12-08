from utils import get_input_lines
import math
import statistics
from functools import lru_cache

input = [int(n) for n in get_input_lines('7.txt')[0].split(',')]
# input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

median = statistics.median_low(input)
s = 0
for crab in input:
    s += abs(median - crab)

print(f'Answer 1: {s}')


@lru_cache(None)
def arithmetic_sum(n):
    a1 = 1
    an = a1 + (n - 1)

    s = n * (a1 + an) / 2
    return int(s)


mean = math.floor(statistics.mean(input))
s = 0
for crab in input:
    s += arithmetic_sum(abs(mean - crab))

print(f'Optimized answer 2: {s}')

max_crab = max(input)

ms = float('inf')
for test_crab in range(max_crab + 1):
    s = 0
    for crab in input:
        s += arithmetic_sum(abs(test_crab - crab))

    ms = min(s, ms)

print(f'Answer 2: {ms}')
