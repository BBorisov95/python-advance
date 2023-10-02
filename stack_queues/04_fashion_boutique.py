box = list(map(int, input().split()))
cap_of_rack = int(input())

racks = 0

while box:
    racks += 1
    current_rack = cap_of_rack
    while box and box[-1] <= current_rack:
        current_rack -= box.pop()

print(racks)