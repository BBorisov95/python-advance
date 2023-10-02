stack = []


for _ in range(int(input())):
    """
    1 - push number into stack
    2 - delete number at the top of the stack
    3 - print the maximum number in the stack
    4 - print the minimum number in the stack
    """

    opr, *data = input().split(' ')

    if opr == '1':
        stack.append(int(data[0]))
    elif opr == '2':
        if len(stack) > 0:
            stack.pop()
    elif opr == '3':
        if len(stack) > 0:
            print(max(stack))
    elif opr == '4':
        if len(stack) > 0:
            print(min(stack))

print(', '.join(map(str, reversed(stack))))
