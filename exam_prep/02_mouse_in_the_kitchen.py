def is_valid_move(row, col):
    return 0 <= row < n and 0 <= col < m

n, m = [int(x) for x in input().split(',')]

matrix = []
mouse_position = None
total_cheeses = 0
eaten_cheeses = 0

for row_index in range(n):
    data = list(input())
    matrix.append(data)
    if "M" in data:
        mouse_position = [row_index, data.index('M')]
    if "C" in data:
        total_cheeses += data.count('C')

direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()

while command != 'danger':

    row_to_move, col_to_move = direction_mapper[command]
    desired_row = mouse_position[0] + row_to_move
    desired_col = mouse_position[1] + col_to_move

    if not is_valid_move(desired_row, desired_col):
        print('No more cheese for tonight!')
        break


    elif matrix[desired_row][desired_col] == '*':
        matrix[desired_row][desired_col] = 'M'
        matrix[mouse_position[0]][mouse_position[1]] = '*'
        mouse_position = [desired_row, desired_col]

    elif matrix[desired_row][desired_col] == 'C':
        matrix[desired_row][desired_col] = 'M'
        matrix[mouse_position[0]][mouse_position[1]] = '*'
        mouse_position = [desired_row, desired_col]
        eaten_cheeses += 1
        if total_cheeses == eaten_cheeses:
            print('Happy mouse! All the cheese is eaten, good night!')
            break

    elif matrix[desired_row][desired_col] == 'T':
        matrix[desired_row][desired_col] = 'M'
        matrix[mouse_position[0]][mouse_position[1]] = '*'
        mouse_position = [desired_row, desired_col]
        print('Mouse is trapped!')
        break

    elif matrix[desired_row][desired_col] == '@':
        command = input()
        continue

    command = input()

else:
    print('Mouse will come back later!')

for rows in matrix:
    print(*rows, sep='')
