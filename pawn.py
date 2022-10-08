# return coordinates of destination : x, y
# you are on 1, 1
# you are on size * size of chess board
current = [1, 1]
size = 5
instructions = 'R R R U D D'
moves = {
    'R': [0, 1],
    'D': [1, 0],
    'L': [0, -1],
    'U': [-1, 0]
}
chess_board = [[x for x in range(size+1)] for y in range(size+1)]
print('chess board', chess_board)

for instruction in instructions.split():
    move = moves[instruction]
    print(' current ', current)
    print(' direction', instruction)
    expectedX = current[0] + move[0]
    expectedY = current[1] + move[1]
    if 1 > expectedX or expectedX > size or 1 > expectedY or expectedY > size:
        print('cleared')
        continue
    current[0] = expectedX
    current[1] = expectedY
    print('moved to ', current)

print(current)
