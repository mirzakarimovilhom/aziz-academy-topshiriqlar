n = int(input())
for x in map(int, input().split()):
    if x % 2 == 0 and x > 0:
        print(x)