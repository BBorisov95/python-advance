
even_set = set()
odd_set = set()

for i in range(1, int(input()) + 1):
    name = input()
    ascii_sum = 0
    for char in name:
        ascii_sum += ord(char)

    div = ascii_sum // i

    if div % 2 == 0:
        even_set.add(div)
    else:
        odd_set.add(div)


even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)
if even_set_sum == odd_set_sum:
    union_of_set = odd_set.union(even_set)
    print(', '.join([str(x) for x in union_of_set]))
elif odd_set_sum > even_set_sum:
    diff_values = odd_set.difference(even_set)
    print(', '.join([str(x) for x in diff_values]))
elif even_set_sum > odd_set_sum:
    symm_diff = odd_set.symmetric_difference(even_set)
    print(', '.join([str(x) for x in symm_diff]))

