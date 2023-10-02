matrix = []
shooter_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            shooter_position = [row, col]
        elif matrix[row][col] == 'x':
            targets += 1

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

targets_down = []

num_of_commands = int(input())

for _ in range(num_of_commands):
    command = input().split()
    if command[0] == 'shoot':
        r = shooter_position[0] + possible_moves[command[1]][0]
        c = shooter_position[1] + possible_moves[command[1]][1]

        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets -= 1
                targets_down.append([r, c])
                break
            r += possible_moves[command[1]][0]
            c += possible_moves[command[1]][1]

        if targets == 0:
            print(f'Training completed! All {len(targets_down)} targets hit.')
            break
    elif command[0] == 'move':
        steps = command[2]
        direction = command[1]
        if direction == 'up':
            r = shooter_position[0] - int(steps)
            c = shooter_position[1]
        elif direction == 'down':
            r = shooter_position[0] + int(steps)
            c = shooter_position[1]
        elif direction == 'left':
            r = shooter_position[0]
            c = shooter_position[1] - int(steps)
        elif direction == 'right':
            r = shooter_position[0]
            c = shooter_position[1] + int(steps)

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[shooter_position[0]][shooter_position[1]] = '.'
            shooter_position = [r,c]

if targets > 0:
    print(f'Training not completed! {targets} targets left.')
[print(row) for row in targets_down]
