import sys


d = list(map(int, sys.stdin.read().split()))
if len(d) == 1:
    print(d[0])
else:
    for _ in range(d[0]):
        print(*range(1, d[1] + 1))