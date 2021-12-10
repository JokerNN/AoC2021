from typing import Optional, Tuple, Union
from utils import get_input_lines

input = get_input_lines('10.txt')

brackets_map = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}


def check_brackets(line: str) -> Tuple[bool, Optional[str]]:
    stack = []
    for char in line:
        if char in brackets_map:
            stack.append(brackets_map[char])
        elif stack[-1] == char:
            stack.pop()
        else:
            return (False, char)

    return (True, None)


scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
for line in input:
    res = check_brackets(line)
    if not res[0]:
        score += scores[res[1]]

print(f'Answer 1: {score}')


scores2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def complete_brackets(line: str) -> Tuple[bool, Union[str, int]]:
    stack = []
    for char in line:
        if char in brackets_map:
            stack.append(brackets_map[char])
        elif stack[-1] == char:
            stack.pop()
        else:
            return (False, char)

    score = 0
    for char in stack[::-1]:
        score = score * 5 + scores2[char]

    return (True, score)


complete_scores = []
for line in input:
    res = complete_brackets(line)
    if res[0] == True:
        complete_scores.append(res[1])

ans2 = sorted(complete_scores)[len(complete_scores) // 2]
print(f'Answer 2: {ans2}')
