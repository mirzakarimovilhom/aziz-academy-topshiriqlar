n, m = map(int, input().split())


for i in range(n):
    print('*' * m if i in (0, n - 1) else '*' + '.' * (m - 2) + '*')