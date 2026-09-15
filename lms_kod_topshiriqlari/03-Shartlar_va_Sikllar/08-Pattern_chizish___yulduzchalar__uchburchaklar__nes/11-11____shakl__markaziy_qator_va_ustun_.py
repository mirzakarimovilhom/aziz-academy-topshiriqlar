n = int(input())
m = n // 2


for i in range(n):
    print('*' * n if i == m else '.' * m + '*' + '.' * m)