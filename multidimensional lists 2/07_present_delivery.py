presents = int(input())
neighborhood = int(input())

matrix = []
santa_location = []
nice_kids = 0
for row in range(neighborhood):
    matrix.append(input().split())
    for col in range(neighborhood):
        if matrix[row][col] == 'S':
            matrix[row][col] = '-'
            santa_location = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids += 1


possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

happy_kids = 0


while presents>0 and nice_kids >= happy_kids:
    command = input()
    if command == 'Christmas morning':
        break

    if 0 <= santa_location[0] + possible_moves[command][0] <= neighborhood - 1 \
            and 0 <= santa_location[1] + possible_moves[command][1] <= neighborhood - 1:
        santa_location[0] = santa_location[0] + possible_moves[command][0]
        santa_location[1] = santa_location[1] + possible_moves[command][1]
        if matrix[santa_location[0]][santa_location[1]] == 'V':
            presents -= 1
            happy_kids += 1
            matrix[santa_location[0]][santa_location[1]] = '-'
        elif matrix[santa_location[0]][santa_location[1]] == 'C':
            for k in possible_moves:
                s_r = santa_location[0] + possible_moves[k][0]
                s_c = santa_location[1] + possible_moves[k][1]
                if 0 <= s_r <= neighborhood - 1 and 0 <= s_c <= neighborhood - 1 and presents:
                    if matrix[s_r][s_c] != "-":
                        if matrix[s_r][s_c] == "V":
                            happy_kids += 1
                        presents -= 1
                        matrix[s_r][s_c] = '-'
        else:
            matrix[santa_location[0]][santa_location[1]] = '-'


if not presents and happy_kids < nice_kids:
    print(f'Santa ran out of presents!')

matrix[santa_location[0]][santa_location[1]] = 'S'


[print(*row) for row in matrix]
if happy_kids == nice_kids:
    print(f'Good job, Santa! {nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - happy_kids} nice kid/s.')