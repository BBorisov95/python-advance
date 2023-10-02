def is_valid_move(row, col):
    return 0 <= row < rows and 0 <= col < columns

def moveing(row, col, direction):
    if direction == 'U':
        row -= 1
    elif direction == 'D':
        row += 1
    elif direction == 'L':
        col -= 1
    elif direction == 'R':
        col += 1
    return row, col

def spread_bunnies(matrix):
    new_bunnies = []
    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == 'B':
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc
                    if is_valid_move(new_row, new_col):
                        new_bunnies.append((new_row, new_col))
    for row, col in new_bunnies:
        if matrix[row][col] == 'P':
            is_dead = True
        matrix[row][col] = 'B'

rows, columns = list(map(int ,input().split()))

matrix = [list(input()) for _ in range(rows)]

current_row, current_col = [(r, c) for r in range(rows) for c in range(columns) if matrix[r][c] == 'P'][0]
is_dead = False
won = False

commands = [str(x) for x in input()]

for command in commands:
    new_row, new_col = moveing(current_row, current_col, command)
    if is_valid_move(new_row, new_col):
        matrix[current_row][current_col] = '.'
        spread_bunnies(matrix)
        if matrix[new_row][new_col] != 'B':
            current_row, current_col = new_row, new_col
            matrix[current_row][current_col] = 'P'
        else:
            current_row, current_col = new_row, new_col
            is_dead = True
            matrix[current_row][current_col] = 'B'
            break
    else:
        matrix[current_row][current_col] = '.'
        won = True
        spread_bunnies(matrix)
        break


[print(*row, sep='') for row in matrix]
if won:
    print(f'won: {current_row} {current_col}')
if is_dead:
    print(f'dead: {current_row} {current_col}')