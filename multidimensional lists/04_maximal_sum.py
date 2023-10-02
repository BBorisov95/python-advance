rows, columns = list(map(int, input().split()))

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')

max_row = 0
max_colum = 0

for row in range(rows - 2):
    for colum in range(columns -2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(colum, colum + 3):
                current_sum += matrix[r][c]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row
            max_colum = colum

print(f'Sum = {max_sum}')
sub_matrix_start = [matrix[r][max_colum:max_colum+3] for r in range(max_row, max_row + 3)]
[print(*row) for row in sub_matrix_start]

