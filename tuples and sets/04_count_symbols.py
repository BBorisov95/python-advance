word = input()

dict_of_occurrences = {}

for el in word:
    if el not in dict_of_occurrences:
        dict_of_occurrences[el] = 1
    else:
        dict_of_occurrences[el] += 1


keys = list(dict_of_occurrences.keys())
keys.sort()
sorted_dict = {i: dict_of_occurrences[i] for i in keys}
for k,v in sorted_dict.items():
    print(f'{k}: {v} time/s')