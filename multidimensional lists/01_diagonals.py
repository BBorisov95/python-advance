rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

primary_diagonal = [matrix[i][i]for i in range(rows)]

secondary_diagonal = [matrix[i][-i - 1]for i in range(rows)] #-i -1 for 1st is 0-1 = index -1

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')