from collections import deque

monster_armor = deque(map(int, input().split(',')))
solder_strike = deque(map(int, input().split(',')))

killed_monsters = 0

while monster_armor and solder_strike:

    current_monster_value = monster_armor.popleft()
    current_solder_strike = solder_strike.pop()

    if current_solder_strike >= current_monster_value:
        killed_monsters += 1
        current_solder_strike -= current_monster_value
        if not solder_strike and current_solder_strike > 0:
            solder_strike.append(current_solder_strike)
        elif solder_strike:
            solder_strike[-1] += current_solder_strike
    else:
        current_monster_value -= current_solder_strike
        monster_armor.append(current_monster_value)

if not monster_armor:
    print('All monsters have been killed!')
if not solder_strike:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {killed_monsters}')
