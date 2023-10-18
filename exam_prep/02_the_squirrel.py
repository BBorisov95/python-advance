def is_valid_index(row, col):
    return 0 <= row < size and 0 <= col < size

HAZELNUTS_TO_OBTAIN = 3

size = int(input())
directions = input().split(', ')

matrix = []

squirrel_position = None

for row_index in range(size):
    data = list(input())
    matrix.append(data)
    if 's' in data:
        squirrel_position = [row_index, data.index('s')]


directions_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
    }

collected_hazelnuts = 0

for direction in directions:

    desired_row, desired_col = directions_mapper[direction]
    matrix[squirrel_position[0]][squirrel_position[1]] = '*'

    if not is_valid_index(squirrel_position[0]+desired_row, squirrel_position[1]+desired_col):
        print('The squirrel is out of the field.')
        break

    squirrel_position = [squirrel_position[0]+desired_row, squirrel_position[1]+desired_col]

    if matrix[squirrel_position[0]][squirrel_position[1]] == 'h':
        collected_hazelnuts += 1
        if collected_hazelnuts == HAZELNUTS_TO_OBTAIN:
            print('Good job! You have collected all hazelnuts!')
            break
    if matrix[squirrel_position[0]][squirrel_position[1]] == '*':
        continue
    if matrix[squirrel_position[0]][squirrel_position[1]] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break
else:
    print('There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {collected_hazelnuts}')




