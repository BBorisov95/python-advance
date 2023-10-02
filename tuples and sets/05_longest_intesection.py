n = int(input())



longest_intersection = 0
intersection_part = set()

for _ in range(n):
    set_one = set()
    set_two = set()
    first_pair, second_pair = input().split('-')
    firs_start, first_end = first_pair.split(',')
    second_start, second_end = second_pair.split(',')
    for i in range(int(firs_start), int(first_end) + 1):
        set_one.add(i)

    for z in range(int(second_start), int(second_end) + 1):
        set_two.add(z)

    current_intersection = set_one.intersection(set_two)
    if len(current_intersection) > longest_intersection:
        longest_intersection = len(current_intersection)
        intersection_part = current_intersection

print(f'Longest intersection is {[x for x in intersection_part]} with length {longest_intersection}')


