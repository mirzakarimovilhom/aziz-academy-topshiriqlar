n, m = map(int, input().split())


for i in range(n):
    print(("*." * m)[i % 2 : i % 2 + m])