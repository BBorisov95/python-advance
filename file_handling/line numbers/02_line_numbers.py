from string import punctuation

res = []

with open('text.txt', 'r') as i_f, open('output.txt', 'w') as o_f:
    for row_index, line in enumerate(i_f):
        letters = 0
        punct = 0
        for char in line:
            if char.isalpha():
                letters += 1
            elif char in punctuation:
                punct += 1
        res.append(f'Line {row_index}: {line.strip()} ({letters})({punct})')
    o_f.write('\n'.join(res))
