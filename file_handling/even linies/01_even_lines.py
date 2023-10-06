
with open('text.txt', 'r') as f:
    for row_index, line in enumerate(f.readlines()):
        if row_index % 2 == 0:
            for char in ',.-?!':
                line = line.replace(char, '@')
            print(' '.join(reversed(line.split())))
