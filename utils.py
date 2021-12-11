from typing import NamedTuple, List

def get_input_lines(filename: str) -> List[str]:
    lines = []
    with open(f'inputs/{filename}') as input_file:
        lines = input_file.read().strip().split('\n')

    return lines


class Point(NamedTuple):
    x: int = 0
    y: int = 0