from collections import deque

tools = deque(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))

while tools and substances and challenges:

    first_tool = tools.popleft()
    last_substances = substances.pop()

    tool_multiply_substances_values = first_tool * last_substances

    for challenge in challenges:
        if tool_multiply_substances_values == challenge:
            challenges.remove(challenge)
            break
    else:
        first_tool += 1
        tools.append(first_tool)
        last_substances -= 1
        if last_substances > 0:
            substances.append(last_substances)

if challenges:
    print('Harry is lost in the temple. Oblivion awaits him.')
else:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f'Tools: {", ".join(str(x) for x in tools)}')
if substances:
    print(f'Substances: {", ".join(str(x) for x in substances)}')
if challenges:
    print(f'Challenges: {", ".join(str(x) for x in challenges)}')