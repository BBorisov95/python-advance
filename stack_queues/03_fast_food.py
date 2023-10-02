from collections import deque
avlb_food = int(input())
queue_for_order = deque(map(int, input().split(' ')))

"""
Find and print the biggest order
"""
if queue_for_order:
    print(max(queue_for_order))
    order = queue_for_order[0]

    while avlb_food >= order:
        if queue_for_order:
            avlb_food -= queue_for_order.popleft()
            if queue_for_order:
                order = queue_for_order[0]
        else:
            print('Orders complete')
            break
    else:
        print(f"Orders left: {' '.join(map(str, queue_for_order))}")




