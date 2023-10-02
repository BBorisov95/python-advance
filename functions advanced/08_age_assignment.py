def age_assignment(*args, **kwargs):
    name_map = []
    for k,v in kwargs.items():
        for arg in args:
            if k == arg[0]:
                name_map.append((arg, v))
    sorted_result = sorted(name_map, key=lambda item: item[0])
    result = []
    for pair in sorted_result:
        result.append(f'{pair[0]} is {pair[1]} years old.')
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))