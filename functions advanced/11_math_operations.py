def math_operations(*numbers, **operations):
    for index, number in enumerate(numbers):
        key = list(operations.keys())[index % 4]  # [index % 4] because operations are 4 a,d,m,s

        if key == "a":
            operations[key] += number

        elif key == "s":
            operations[key] -= number

        elif key == "d" and number != 0:
            operations[key] /= number

        elif key == "m":
            operations[key] *= number

    operations = dict(sorted(operations.items(), key=lambda x: (-x[1], x[0])))
    result = "\n".join(f"{key}: {value:.1f}" for key, value in operations.items())
    return result

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))