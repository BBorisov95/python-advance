from collections import deque
def fill_the_box(height, length, width, *args):
    """
    cube is exact size or 1x1x1
    """
    box_size = height * length * width
    cubes = deque(args)
    while cubes:
        if cubes[0] == 'Finish':
            break
        cub = cubes.popleft()
        if box_size > 0 and cub <= box_size:
            box_size -= cub
        elif box_size > 0 and cub > box_size:
            left_cube = cub - box_size
            box_size -= box_size
            cubes.appendleft(left_cube)
        else:
            left_cubes = cub
            for cub in cubes:
                if cub != 'Finish':
                    left_cubes += cub
            return f'No more free space! You have {left_cubes} more cubes.'
    if len(cubes) > 0:
        return f'There is free space in the box. You could put {box_size} more cubes.'



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))