from collections import deque

maze = [
    ['S', '#', ' ', ' ', ' ', ' ', ' ', '#', ' '],
    [' ', '#', ' ', '#', '#', ' ', ' ', '#', ' '],
    [' ', '#', ' ', '#', 'G', ' ', ' ', '#', ' '],
    [' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' '],
    [' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' '],
    [' ', '#', ' ', '#', '#', '#', ' ', ' ', ' '],
    [' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' '],
    [' ', '', ' ', '#', '#', '#', ' ', ' ', ' '],
    [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

def is_valid(x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

def find_goal(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'G':
                return (i, j)

def bfs(maze):
    start = (0, 0)
    goal = find_goal(maze)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path + [(x, y)]

        visited.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), path + [(x, y)]))

path = bfs(maze)
if path:
    print("Path from S to G:")
    for x, y in path:
        maze[x][y] = '*'
        for row in maze:
            print("".join(row))
else:
    print("No path found")
