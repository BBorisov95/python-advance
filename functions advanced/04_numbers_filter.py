def even_odd_filter(**kwargs):
    result = {}
    for arg, values in kwargs.items():
        if arg == 'even':
            if arg not in result:
                result[arg] = {}
            result[arg] = [x for x in values if x%2 == 0]
        if arg == 'odd':
            if arg not in result:
                result[arg] = {}
            result[arg] = [x for x in values if x%2 != 0]
    sorted_result = dict(sorted(result.items(), key=lambda kvp: kvp[0][0]))
    return sorted_result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
