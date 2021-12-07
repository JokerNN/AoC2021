input = []

import re

with open('inputs/4.txt') as input_file:
    input = input_file.read().strip().split('\n\n')

nums = [int(num) for num in input[0].split(',')]
# print(nums)

del input[0]



def mark_num(board, num):
    for row in board:
        for cell in row:
            if cell[0] == num:
                cell[1] = True

def check_board_for_win(board):
    for row in board:
        if all(cell[1] for cell in row):
            return True
    for idx in range(len(board[0])):
        if all(row[idx][1] for row in board):
            return True

def calc_winning_score(board):
    s = 0
    for row in board:
        for cell in row:
            if cell[1] != True:
                s += cell[0]

    return s

boards = []
for board_str in input:
    board = []
    for row in board_str.split('\n'):
        board.append([[int(num), False] for num in re.split(r' +', row.strip())])

    boards.append(board)


board_found = False
for num in nums:
    if board_found:
        break
    for board in boards:
        mark_num(board, num)
        if (check_board_for_win(board)):
            board_found = True
            print(f'Answer 1: {calc_winning_score(board) * num}')
            break



boards = []
for board_str in input:
    board = []
    for row in board_str.split('\n'):
        board.append([[int(num), False] for num in re.split(r' +', row.strip())])

    boards.append(board)

won_boards = []
boards_set = set()
for num in nums:
    for idx, board in enumerate(boards):
        if idx in boards_set:
            continue
        mark_num(board, num)
        if (check_board_for_win(board)):
            boards_set.add(idx)
            won_boards.append([board, num])

last_board, last_num = won_boards[-1]
print(f'Answer 2: {calc_winning_score(last_board) * last_num}')