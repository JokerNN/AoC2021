from utils import get_input_lines

input = get_input_lines('8.txt')

total_1478 = 0
for line in input:
    inp, out = line.split(' | ')
    for dig in out.strip().split(' '):
        if len(dig) in {2, 4, 3, 7}:
            total_1478 += 1


print(f'Answer 1: {total_1478}')


#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg


# input = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

num_sum = 0
for line in input:
    inp, out = line.split(' | ')
    inp = [''.join(sorted(token)) for token in inp.split(' ')]
    out = [''.join(sorted(token)) for token in out.split(' ')]
    tokens = set([*inp, *out])
    # find 1, 4, 7 and 8
    one, two, three, four, five, six, seven, eight, nine, zero = [None] * 10
    token_map = {}
    for token in tokens:
        if len(token) == 2:
            one = token
        elif len(token) == 3:
            seven = token
        elif len(token) == 4:
            four = token
        elif len(token) == 7:
            eight = token

    token_map['a'] = (set(seven) - set(one)).pop()

    # find six
    for token in tokens:
        if len(token) == 6 and len(set(token) & set(one)) == 1:
            six = token
            break

    token_map['f'] = (set(six) & set(one)).pop()
    token_map['c'] = (set(one) - set(token_map['f'])).pop()

    # find two and five

    for token in tokens:
        if len(token) == 5:
            if token_map['c'] in token and token_map['f'] not in token:
                two = token
            elif token_map['f'] in token and token_map['c'] not in token:
                five = token
            elif token_map['c'] in token and token_map['f'] in token:
                three = token

    if (five == two):
        raise Exception('Wrong')

    if not two or not five:
        raise Exception("Can't find two or five")

    token_map['e'] = (set(eight) - set(five) - {token_map['c']}).pop()
    token_map['b'] = (set(eight) - set(two) - {token_map['f']}).pop()

    # find nine

    for token in tokens:
        if len(token) == 6 and token_map['e'] not in set(token):
            nine = token
            break

    if not nine:
        raise Exception("Can't find nine")

    # find zero

    for token in tokens:
        if len(token) == 6 and token != six and token != nine:
            zero = token
            break

    # now we know all digits
    digit_map = {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six:  '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }

    num = []

    for token in out:
        num.append(digit_map[token])

    num = int(''.join(num))
    num_sum += num

print(f'Answer 2: {num_sum}')
