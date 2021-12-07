def get_input_lines(filename):
    lines = []
    with open(f'inputs/{filename}') as input_file:
        lines = input_file.read().strip().split('\n')

    return lines