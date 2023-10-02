from collections import deque

n = deque(input())

open_symbols = '{[('
closing_symbols = '}])'

count = 0

while n and count < len(n) / 2:
    if n[0] not in open_symbols:
        break
    index = open_symbols.index(n[0])
    """
    get the expression first symbol index in our open symbols
    """
    if n[1] == closing_symbols[index]:
        n.popleft()
        n.popleft()
        n.rotate(count)
        count = 0
    else:
        """
        if first 2 symbols are not matching rotate the n 
        """
        n.rotate(-1)
        count += 1

if n:
    print('NO')
else:
    print("YES")