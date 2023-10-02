from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

needed_points = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_toys = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in needed_points:
        toy = needed_points[total_magic]
        if toy not in crafted_toys:
            crafted_toys[toy] = 0
        crafted_toys[toy] += 1
        materials.pop()
        magic.popleft()
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()

if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or ('Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials[::-1]])}')
if magic:
    print(f'Magic left: {", ".join(str(x) for x in magic)}')

for k,v in sorted(crafted_toys.items()):
    if v > 0:
        print(f'{k}: {v}')

