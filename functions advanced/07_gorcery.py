def grocery_store(**kwargs):
    sorting_dict = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    res = []
    for product, quantity in sorting_dict.items():
        res.append(f'{product}: {quantity}')
    return '\n'.join(res)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
