import sys


data = list(map(int, sys.stdin.read().split()))
k = data[-1]
a = data[1:-1]
print(min(a, key=lambda x: (abs(x - k), x)))