from collections import deque
from datetime import datetime, timedelta

robot_data = input().split(';')
start_time = datetime.strptime(input(), '%H:%M:%S')
robots = {}

for robot in robot_data:
    robot_name, robot_process_time = robot.split('-')
    if robot_name not in robots:
        robots[robot_name] = [int(robot_process_time), start_time]

items = deque()
seconds_passed = 0

while True:
    command = input()
    if command == "End":
        break
    items.append(command)

while items:
    seconds_passed += 1
    current_time = start_time + timedelta(seconds=seconds_passed)

    for robot in robots:
        if robots[robot][1] <= current_time:
            print(f"{robot} - {items[0]} [{current_time.strftime('%H:%M:%S')}]")
            items.popleft()
            robots[robot][1] = current_time + timedelta(seconds=robots[robot][0])
            break
    else:
        items.rotate(-1)
