n, m = [int(num) for num in input().split()]
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())


print('\n'.join(n_set.intersection(m_set)))