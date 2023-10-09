class FullColumnError(Exception):
    pass



ROWS = 6
COLS = 7


direction_mapper = {
    (-1, 0), # Up
    (0, 1), # Right
    (-1, 1), # Up right
    (-1, -1), # Up left
}

def print_matrix(matrix):
    for row in matrix:
        print(row)


def is_valid_colum_choice(selected_column):
    return 0 <= selected_column < COLS


def place_player_number(colum_index, matrix, player_number):
    for row_index in range(ROWS-1, -1, -1):
        if matrix[row_index][colum_index] == 0:
            matrix[row_index][colum_index] = player_number
            return row_index, colum_index
    else:
        raise FullColumnError


def requested_dir_count(current_row, row_move, current_column, col_move, matrix, player):
    count = 1
    for i in range(1, 4):
        row_index_to_check = current_row + row_move * i
        col_index_to_check = current_column + col_move * i
        if not is_valid_place(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player:
            break
        count += 1
    return count

def opposite_dir_count(current_row, row_move, current_column, col_move, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row - row_move * i
        col_index_to_check = current_column - col_move * i
        if not is_valid_place(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player:
            break

        count += 1
    return count

def is_winner(current_row, current_column, matrix, player):
    for row_move, col_move in direction_mapper:
        count_dir = requested_dir_count(current_row, row_move, current_column, col_move, matrix, player)
        count_opposite_dir = opposite_dir_count(current_row, row_move, current_column, col_move, matrix, player)
        if count_dir + count_opposite_dir >= 4:
            return True
        return False



def is_valid_place(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS

matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
print_matrix(matrix)

player = 1
while True:
    try:
        selected_colum = int(input(f"Player {player}, please choose a column: "))-1
        if not is_valid_colum_choice(selected_colum):
            raise ValueError
        current_row, current_colum = place_player_number(selected_colum, matrix, player)

        if is_winner(current_row, current_colum, matrix, player):
            print_matrix(matrix)
            print(f'The winnder is {player}')
            break
        print_matrix(matrix)
    except ValueError:
        print(f'Player: {player} - Please select number between 1 and {COLS}')
        continue
    except FullColumnError:
        print(f'Player: {player} - this column is full. Please select another column')
        continue

    player += 1
    player = 2 if player % 2 == 0 else 1