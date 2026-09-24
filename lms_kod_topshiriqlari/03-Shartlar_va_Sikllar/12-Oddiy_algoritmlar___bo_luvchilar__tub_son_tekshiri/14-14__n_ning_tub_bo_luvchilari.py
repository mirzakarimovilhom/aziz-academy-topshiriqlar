n = int(input())


for i in range(2, n + 1):
    if n % i == 0 and all(i % j != 0 for j in range(2, i)):
        print(i)