def is_valid_sign(player_one_sign):
    return player_one_sign in ['X', "O"]


def print_board(board):
    for row in board:
        print('| ', end='')
        print(' | '.join([char if char else ' ' for char in row]), end='')
        print(' |')


def is_row_win(board):
    for row in board:
        if len(set(row)) == 1 and set(row) != {None}:
            return True
    return False


def is_colum_win(board, current_sign):
    for col in range(len(board)):
        current_column = []
        for row in range(len(board)):
            current_column.append(board[row][col] == current_sign)
        if all(current_column):
            return True
    return False


def is_diagonal_win(board, current_sign):
    diag_1, diag_2 = [], []
    for i in range(len(board)):
        diag_1.append(board[i][i] == current_sign)
        diag_2.append(board[i][len(board) - 1 - i] == current_sign)
    return all(diag_1) or all(diag_2)


def is_win(board, current_sign):
    return any([is_row_win(board),
                is_colum_win(board, current_sign),
                is_diagonal_win(board, current_sign)])


def is_row_win_possible(board):
    if all(["X" in row and "O" in row for row in board]):
        return False
    return True


def is_colum_win_possible(board):
    columns = []
    for col in range(len(board)):
        current_column = []
        for row in range(len(board)):
            current_column.append(board[row][col])
        columns.append(current_column)
    if all(["X" in col and "O" in col for col in columns]):
        return False
    return True


def is_diagonal_win_possible(board):
    diag_1, diag_2 = [], []
    for i in range(len(board)):
        diag_1.append(board[i][i])
        diag_2.append(board[i][len(board) - 1 - i])
    if "X" in diag_1 and 'O' in diag_1 and "x" in diag_1 and "O" in diag_2:
        return False
    return True


def is_draw(board):
    if any([is_row_win_possible(board),
           is_colum_win_possible(board),
           is_diagonal_win_possible(board)
            ]):
        return False
    return True


def is_valid_choice(board, board_mapper, choice):
    if not choice.isdigit():
        return False
    choice = int(choice)
    if choice not in board_mapper:
        return False
    if board[board_mapper[choice][0]][board_mapper[choice][1]]:
        return False
    return True



player_one = input('Player one name: ').strip()
player_two = input('Player two name: ').strip()


while True:
    player_one_sign = input(f"{player_one}, would you like to play with 'X' or 'O'").upper()
    if is_valid_sign(player_one_sign):
        break
    print('Please enter one of the following "X" or "O"')

player_two_sign = 'X' if player_one_sign == 'O' else 'O'

size = 3
board = [[None] * size for _ in range(size)]
#               i // size == row ; i % size == column;
board_mapper = {i+1: (i // size, i % size)for i in range(size ** 2)}


print('This is the numeration of the board')
[print(f'| {" | ".join([str(i+1+row*size) for i in range(size)])} |')for row in range(size)]
print(f'{player_one} starts first')

turn = 1

while True:
    current_player = player_one if turn % 2 else player_two
    current_sign = player_one_sign if turn % 2 else player_two_sign
    while True:
        choice = input(f'{current_player} please choose position between 1 and {size ** 2}: ').strip()
        if is_valid_choice(board, board_mapper, choice):
            break
    row, col = board_mapper[int(choice)]
    board[row][col] = current_sign
    print_board(board)
    if is_win(board, current_sign):
        print(f"{current_sign} Won")
        break
    if is_draw(board):
        print("Draw")
        break

    turn += 1

