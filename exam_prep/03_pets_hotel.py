def accommodate_new_pets(capacity: int, max_weight: float, *args):
    string_to_print = ''
    accomodated_pets = {}
    for pet_type, weight in args:
        if capacity <= 0:
            string_to_print += 'You did not manage to accommodate all pets!\n'
            break
        if weight > max_weight:
            continue
        if pet_type not in accomodated_pets:
            accomodated_pets[pet_type] = 0
        accomodated_pets[pet_type] += 1
        capacity -= 1
    else:
        string_to_print += f'All pets are accommodated! Available capacity: {capacity}.\n'

    string_to_print += 'Accommodated pets:\n'
    for pet, count in sorted(accomodated_pets.items()):
        string_to_print += f'{pet}: {count}\n'

    return string_to_print[:-1]


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
