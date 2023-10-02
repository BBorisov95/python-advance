def find_numb(numbs):
    sum_positive = 0
    sum_negative = 0
    for num in numbs:
        if num < 0:
            sum_negative += num
        else:
            sum_positive += num
    return sum_positive, sum_negative

numbs = [int(x) for x in input().split()]

sum_positive, sum_negative = find_numb(numbs)

print(sum_negative)
print(sum_positive)

if abs(sum_negative) > sum_positive:
    print("The negatives are stronger than the positives")
else:
    print('The positives are stronger than the negatives')