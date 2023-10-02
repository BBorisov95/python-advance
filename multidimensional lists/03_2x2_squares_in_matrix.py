rows, columns = list(map(int, input().split()))

matrix = [[x for x in input().split()] for _ in range(rows)]

count = 0

for row in range(rows - 1):
    for colum in range(columns - 1):
        if matrix[row][colum] == matrix[row][colum + 1] == matrix[row+1][colum] == matrix[row +1][colum + 1]:
            count += 1

print(count)
    