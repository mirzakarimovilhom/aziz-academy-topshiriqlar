n, m = map(int, input().split())
print(*(i**2 for i in range(n, m + 1)))