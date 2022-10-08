from collections import deque

cube = [
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]
possible_move = [
    # y axis , x axis
    [0, -1],
    [0, 1],
    [1, 0],
    [-1, 0],
]
count = 0


def count_cube_ice(cube):
    global count
    y_len = len(cube)

    for y in range(y_len):
        row = cube[y]
        for x in range(len(row)):
            # entry point for search
            print('entry', y, x)
            if not cube[y][x]:
                print(' ... ', cube)
                count += 1
                cube[y][x] = 1
                que = deque()
                que.append([y, x])
                while que:
                    curr = que.popleft()
                    for move in possible_move:
                        target_y = curr[0] + move[0]
                        target_x = curr[1] + move[1]

                        if 0 <= target_y < y_len and 0 <= target_x < len(row):
                            if cube[target_y][target_x] == 0:
                                que.append([target_y, target_x])
                                cube[target_y][target_x] = 1


count_cube_ice(cube)
print(count)
print('cube', cube)
