n = int(input())
for i in range(n):
    s = ['.'] * n
    s[i] = s[~i] = '*'
    print(*s, sep='')