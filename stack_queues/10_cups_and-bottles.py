from collections import deque

cups_capacity = deque(int(x) for x in input().split())
bottles_capacity = list(int(x) for x in input().split())

wasted_water = 0

while True:
    if cups_capacity and bottles_capacity:
        current_cup = cups_capacity.popleft()
        current_bottle = bottles_capacity.pop()
        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup
        else:
            cups_capacity.appendleft(current_cup - current_bottle)
    else:
        break

if bottles_capacity:
    #print(f"Bottles: {' '.join([str(bottle) for bottle in bottles_capacity])}")
    print(f'Bottles:', end='')
    while bottles_capacity:
        print(f' {bottles_capacity.pop()}')
else:
    print(f"Cups: {' '.join([str(cup) for cup in cups_capacity])}")

print(f"Wasted litters of water: {wasted_water}")
