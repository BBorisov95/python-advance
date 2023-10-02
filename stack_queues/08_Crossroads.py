# from collections import deque
#
# green_light_period = int(input())
# free_window = int(input())
#
# cars = deque()
# passed_cars = []
#
# while True:
#
#     command = input()
#
#     if command == 'END':
#         print("Everyone is safe.")
#         print(f"{len(passed_cars)} total cars passed the crossroads.")
#         break
#
#     if command == 'green':
#         current_green_light_time = green_light_period
#         current_free_window_time = free_window
#         total_free_time = current_free_window_time + current_green_light_time
#
#         while cars:
#             car = cars[0]
#             temp_car = deque(car)
#
#             while temp_car and total_free_time:
#                 temp_car.popleft()
#                 total_free_time -= 1
#
#             if temp_car:
#                 print("A crash happened!")
#                 print(f"{car} was hit at {temp_car[0]}.")
#                 exit()
#             else:
#                 passed_cars.append(cars.popleft())
#
#             if total_free_time < free_window:
#                 break
#     else:
#         cars.append(command)

from collections import deque

green_light_seconds = int(input())
free_window_seconds = int(input())

cars_queue = deque()
passed_cars = []
crash = False
counter = 0

while True:
    command = input()

    if command == 'END':
        print("Everyone is safe.")
        print(f"{counter} total cars passed the crossroads.")
        break

    if command == 'green':
        green_light = green_light_seconds
        while green_light > 0 and cars_queue:
            car = cars_queue.popleft()
            if len(car) <= green_light:
                green_light -= len(car)
                counter += 1
                passed_cars.append(car)
            elif len(car) <= green_light + free_window_seconds:
                green_light = 0
                free_window_seconds = 0
                counter += 1
                passed_cars.append(car)
            else:
                crash = True
                crash_index = green_light
                print("A crash happened!")
                print(f"{car} was hit at {car[green_light + free_window_seconds]}.")
                break

        if crash:
            break
    else:
        cars_queue.append(command)