def is_valid(row, col, matrix_range):
    return 0 <= row < matrix_range and 0 <= col < matrix_range

field_size = int(input())
commands = input().split()
matrix = []

current_row, current_col = 0, 0
coals = 0
game_over = False


for r in range(field_size):
    matrix.append(input().split())
    for c in range(field_size):
        if matrix[r][c] == 's':
            current_row, current_col = r, c
        elif matrix[r][c] == 'c':
            coals += 1

for command in commands:
    if command == 'up':
        if is_valid(current_row - 1, current_col, field_size):
            current_row -= 1
    elif command == 'down':
        if is_valid(current_row + 1, current_col, field_size):
            current_row += 1
    elif command == 'right':
        if is_valid(current_row, current_col + 1, field_size):
            current_col += 1
    elif command == 'left':
        if is_valid(current_row, current_col - 1, field_size):
            current_col -= 1

    if matrix[current_row][current_col] == 'e':
        print(f'Game over! ({current_row}, {current_col})')
        game_over = True
        break
    elif matrix[current_row][current_col] == 'c':
        coals -= 1
        matrix[current_row][current_col] = '*'
        if coals == 0:
            print(f'You collected all coal! ({current_row}, {current_col})')
            game_over = True
            break

if not game_over:
    print(f'{coals} pieces of coal left. ({current_row}, {current_col})')

