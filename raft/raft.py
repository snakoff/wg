from collections import deque
from random import random


def check_next_node(x, y):
    if 0 <= x < cols and 0 <= y < rows and not grid[y][x]:
        return True
    else:
        return False


def get_next_nodes(x, y):
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    edges = []
    for dx, dy in ways:
        if check_next_node(x + dx, y + dy):
            edges += {(x + dx, y + dy)}
    return edges


def search(start, finish, graph):
    search_queue = deque()
    search_queue += graph[start]
    queue = deque([start])
    searched = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == finish:
            print(str(cur_node) + " is finish")
            return True, searched

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in searched:
                queue.append(next_node)
                searched[next_node] = cur_node
    return False, searched


cols = int(input("cols:\n"))
rows = int(input("rows:\n"))
grid = [[1 if random() < 0.1 else 0 for col in range(cols)] for row in range(rows)]
for line in grid:
    print(line)

start_x, start_y = int(input("start x:\n")),  int(input("start y:\n"))
finish_x, finish_y = int(input("finish x:\n")), int(input("finish y:\n"))

start = (start_x, start_y)
finish = (finish_x, finish_y)


graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

result, searched = search(start, finish, graph)
if result:
    path_segment = finish

    while path_segment and path_segment in searched:
        grid[path_segment[0]][path_segment[1]] = 3
        path_segment = searched[path_segment]

    grid[start[0]][start[1]] = 2
    grid[finish[0]][finish[1]] = 4
    for line in grid:
        print(line)
