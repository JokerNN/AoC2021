from utils import get_input_lines
from copy import copy

input = get_input_lines('3.txt')

least_commons, most_commons = [], []

for idx in range(len(input[0])):
    ones_count, zeroes_count = 0, 0 
    for num in input:
        if num[idx] == '1':
            ones_count += 1
        elif num[idx] == '0':
            zeroes_count += 1

    if ones_count > zeroes_count:
        most_commons.append('1')
        least_commons.append('0')
    elif zeroes_count > ones_count:
        most_commons.append('0')
        least_commons.append('1')

lc = int(''.join(least_commons), 2)
mc = int(''.join(most_commons), 2)
print(f'Answer 1: {mc * lc}')


lc_filter = copy(input)
mc_filter = copy(input)

bit_idx = 0
while len(mc_filter) > 1:
    ones_count, zeroes_count = 0, 0
    for num in mc_filter:
        if num[bit_idx] == '1':
            ones_count += 1
        elif num[bit_idx] == '0':
            zeroes_count += 1

    control_bit = '1'
    if ones_count < zeroes_count:
        control_bit = '0'

    mc_filter = [num for num in mc_filter if num[bit_idx] == control_bit]
    bit_idx += 1

bit_idx = 0
while len(lc_filter) > 1:
    ones_count, zeroes_count = 0, 0
    for num in lc_filter:
        if num[bit_idx] == '1':
            ones_count += 1
        elif num[bit_idx] == '0':
            zeroes_count += 1

    control_bit = '0'
    if ones_count < zeroes_count:
        control_bit = '1'

    lc_filter = [num for num in lc_filter if num[bit_idx] == control_bit]
    bit_idx += 1

lc = int(lc_filter[0], 2)
mc = int(mc_filter[0], 2)
print(f'Answer 2: {lc * mc}')


        
