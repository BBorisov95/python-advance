from collections import deque

rows, columns = list(map(int, input().split()))
txt = deque(input())

matrix = []

for row in range(rows):
    matrix.append([''] * columns)
    for colum in range(columns):
        if row % 2 == 0:
            matrix[row][colum] = txt[0]
        else:
            matrix[row][-1 - colum] = txt[-1]

        txt.rotate(-1)

[print(*row, sep='') for row in matrix]