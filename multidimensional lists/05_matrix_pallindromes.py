rows, columns = list(map(int, input().split()))

start = ord('a')

for row in range(rows):
    for colum in range(columns):
        print(f'{chr(start + row)}{chr(start + row + colum)}{chr(start + row)}', end=' ')
    print()