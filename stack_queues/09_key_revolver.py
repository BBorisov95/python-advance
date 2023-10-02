from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_values = int(input())
used_bullets = 0
shots = 0
while bullets and locks:
    if bullets:
        if bullets.pop() <= locks[0]:
            print('Bang!')
            locks.popleft()
        else:
            print('Ping!')
        shots += 1
        used_bullets += 1

    if bullets and shots == gun_barrel_size:
        print('Reloading!')
        shots = 0

if not locks:
    used_bullets_cost = used_bullets * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${intelligence_values  - used_bullets_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
