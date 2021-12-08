from typing import Optional, Tuple, List
from utils import get_input_lines
from collections import Counter

input = get_input_lines('6.txt')

fish_array = [int(fish) for fish in input[0].split(',')]
# fish_array = [3, 4, 3, 1, 2]


def simulate_fish_tick(fish: int) -> Tuple[int, Optional[int]]:
    if fish == 0:
        return (6, 8)
    else:
        return (fish - 1, None)


def init_empty_tank(max_days: int = 9) -> Counter:
    empty_tank = Counter()
    for day in range(max_days):
        empty_tank[day] = 0

    return empty_tank


def simulate_fish(fish_array: List[int], days: int) -> Counter:
    fish_tank = Counter(fish_array)
    for day in range(9):
        if day not in fish_tank:
            fish_tank[day] = 0

    for _ in range(days):
        next_tank = init_empty_tank()
        for fish in fish_tank.keys():
            if fish_tank[fish] == 0:
                continue
            result = simulate_fish_tick(fish)

            if result[1] is not None:
                next_tank[result[1]] += fish_tank[fish]

            next_tank[result[0]] += fish_tank[fish]

        fish_tank = next_tank

    return fish_tank


res1 = simulate_fish(fish_array, 80)
res2 = simulate_fish(fish_array, 256)
print(f'Answer 1: {sum(res1.values())}')
print(f'Answer 2: {sum(res2.values())}')
