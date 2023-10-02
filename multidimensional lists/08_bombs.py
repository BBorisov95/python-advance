def is_alive(row, col, matrix):
    return matrix[row][col] > 0


def if_go_left(row, col, matrix, rows, dmg):
    if 0 <= col < rows:
        if is_alive(row, col, matrix):
            matrix[row][col] -= dmg


def if_go_right(row, col, matrix, rows, dmg):
    if col <= rows-1:
        if is_alive(row, col, matrix):
            matrix[row][col] -= dmg


def reduce_cells(row, col, dmg, rows):
    matrix[row][col] -= dmg
    if_go_left(row, col-1, matrix, rows, dmg)
    if_go_right(row, col+1, matrix, rows, dmg)

    if row+1 <= rows-1:
        if is_alive(row+1, col, matrix):
            matrix[row+1][col] -= dmg
        if_go_left(row+1, col-1, matrix, rows, dmg)
        if_go_right(row+1, col+1, matrix, rows, dmg)

    if 0 <= row-1 < rows:
        if is_alive(row-1, col, matrix):
            matrix[row-1][col] -= dmg
        if_go_left(row-1, col-1, matrix, rows, dmg)
        if_go_right(row-1, col+1, matrix, rows, dmg)





rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

commands = input().split()

for command in commands:
    row, col = list(map(int, command.split(',')))
    if is_alive(row, col, matrix):
        bomb_values = matrix[row][col]
        reduce_cells(row, col, bomb_values, rows)

alive_cells = 0
sum_alive_cell = 0

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_alive_cell += matrix[row][col]


print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_alive_cell}')
[print(*row) for row in matrix]