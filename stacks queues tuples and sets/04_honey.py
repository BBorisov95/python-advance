from collections import deque
working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(map(str, input().split()))


mapper = {
    '+': lambda bee, nectar: bee + nectar,
    '-': lambda bee, nectar: bee - nectar,
    '*': lambda bee, nectar: bee * nectar,
    '/': lambda bee, nectar: bee / nectar,
}

total_honey = 0
while working_bees and nectar:

    if nectar[-1] <= 0 and working_bees[0] <= 0:
        nectar.pop()
        working_bees.popleft()
        continue

    if symbols[0] == '/' and nectar[-1] == 0:
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()

    if nectar[-1] >= working_bees[0]:
        result = mapper[symbols[0]](working_bees[0], nectar[-1])
        total_honey += abs(result)
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    elif nectar[-1] < working_bees[0]:
        nectar.pop()

print(f'Total honey made: {total_honey}')

if working_bees:
    print(f'Bees left: {", ".join(str(bee) for bee in working_bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')