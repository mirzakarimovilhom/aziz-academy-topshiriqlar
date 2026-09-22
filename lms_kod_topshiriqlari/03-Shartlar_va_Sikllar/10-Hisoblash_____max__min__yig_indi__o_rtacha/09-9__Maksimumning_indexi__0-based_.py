import sys


a = list(map(int, sys.stdin.read().split()[1:]))
print(a.index(max(a)))