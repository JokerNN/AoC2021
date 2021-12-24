from typing import Tuple
from utils import Point
target_area = [Point(70, -124), Point(96, -179)]
# target_area = [Point(20, -5), Point(30, -10)]


def probe_tick(pos: Point, vel: Point) -> Tuple[Point, Point]:
    next_pos = Point(pos.x + vel.x, pos.y + vel.y)
    next_vel_x = 0
    if vel.x > 0:
        next_vel_x = vel.x - 1
    elif vel.x < 0:
        next_vel_x = vel.y + 1

    next_vel = Point(next_vel_x, vel.y - 1)

    return next_pos, next_vel


max_y = 0
count_found = 0
for vel_x in range(1, target_area[1].x + 1):
    for vel_y in range(target_area[1].y - 1, -target_area[1].y + 1):
        pos = Point(0, 0)
        vel = Point(vel_x, vel_y)
        highest_y = 0
        found = False
        while True:
            npos, nvel = probe_tick(pos, vel)

            pos, vel = npos, nvel
            highest_y = max(highest_y, pos.y)

            if target_area[0].x <= pos.x <= target_area[1].x and\
                    target_area[0].y >= pos.y >= target_area[1].y:
                found = True
                break

            if npos.x > target_area[1].x or npos.y < target_area[1].y:
                # print('overshoot')
                break

            pos, vel = npos, nvel

        if (found):
            max_y = max(highest_y, max_y)
            count_found += 1

print(f'Answer 1: {max_y}')
print(f'Answer 2: {count_found}')
