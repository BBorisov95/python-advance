from collections import deque

exp = input().split()
numbs = deque()

for char in exp:
    if char not in '+-*/':
        numbs.append(int(char))
    else:
        while len(numbs) > 1:
            first_el_in_deque = numbs.popleft()
            second_el_in_deque = numbs.popleft()
            if char == '+':
                numbs.appendleft(first_el_in_deque + second_el_in_deque)
            elif char == '-':
                numbs.appendleft(first_el_in_deque - second_el_in_deque)
            elif char == '*':
                numbs.appendleft(first_el_in_deque * second_el_in_deque)
            elif char == '/':
                numbs.appendleft(first_el_in_deque // second_el_in_deque)

print(numbs[0])
