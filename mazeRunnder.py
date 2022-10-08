destination = [4, 5]
maze = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]


def run_to_end(maze, curr, steps):
    if 0 > curr[0] or curr[0] > destination[0] or curr[1] < 0 or curr[1] > destination[1]:
        return 100

    if maze[curr[0]][curr[1]] == 0:
        return 100

    maze[curr[0]][curr[1]] = 0
    steps += 1
    if curr == destination:
        return steps

    y = curr[0]
    x = curr[1]
    up = run_to_end(maze, [y-1, x], steps)
    down = run_to_end(maze, [y+1, x], steps)
    left = run_to_end(maze, [y, x-1], steps)
    right = run_to_end(maze, [y, x+1], steps)

    print(steps, up, down, left, right)
    return min(up, down, left, right)


print(run_to_end(maze, [0, 0], 0))
