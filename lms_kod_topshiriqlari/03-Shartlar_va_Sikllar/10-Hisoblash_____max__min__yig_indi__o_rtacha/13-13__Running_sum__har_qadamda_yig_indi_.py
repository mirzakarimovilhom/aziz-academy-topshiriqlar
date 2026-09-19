import sys


data = list(map(int, sys.stdin.read().split()[1:]))
s = 0
for x in data:
    s += x
    print(s)