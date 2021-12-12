from typing import DefaultDict, List, Set
from utils import get_input_lines

inp = get_input_lines('12.txt')

graph: DefaultDict[str, Set[str]] = DefaultDict(set)

for line in inp:
    node_a, node_b = line.split('-')
    graph[node_a].add(node_b)
    graph[node_b].add(node_a)


def dfs(node: str, path_set: Set[str] = set()) -> int:
    if node == 'start':
        return 1

    s = 0

    for connection in graph[node]:
        if connection.islower():
            if connection not in path_set:
                s += dfs(connection, {*path_set, connection})
        else:
            s += dfs(connection, {*path_set, connection})

    return s


ans1 = dfs('end', path_set={'end'})
print(f'Answer 1: {ans1}')


def dfs2(node: str, path_set: Set[str], twice_cave: bool = False):
    if node == 'start':
        return 1

    s = 0

    for connection in graph[node]:
        if connection.islower():
            if connection not in path_set:
                s += dfs2(connection, {*path_set,
                          connection}, twice_cave)
            elif not twice_cave and connection != 'start' and connection != 'end':
                s += dfs2(connection, path_set, True)
        else:
            s += dfs2(connection, {*path_set, connection},
                      twice_cave)

    return s


ans2 = dfs2('end', {'end'}, False)

print(f'Answer 2: {ans2}')
