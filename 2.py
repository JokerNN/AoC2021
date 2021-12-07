with open('inputs/2.txt') as input_file:
    commands = input_file.read().strip().split('\n')
    x, y = 0, 0
    for command in commands:

        direction, increment = command.split(' ')
        increment = int(increment)
        if direction == 'forward':
            x += increment
        elif direction == 'down':
            y += increment
        elif direction == 'up':
            y -= increment

    print(f'Answer 1: {x * y}')

    aim, depth  = 0, 0
    x, y = 0, 0 

    for command in commands:
        direction, increment = command.split(' ')
        increment = int(increment)
        if direction == 'forward':
            x += increment
            y += aim * increment
        elif direction == 'down':
            aim += increment
        elif direction == 'up':
            aim -= increment

    print(f'Answer 2: {x * y}')