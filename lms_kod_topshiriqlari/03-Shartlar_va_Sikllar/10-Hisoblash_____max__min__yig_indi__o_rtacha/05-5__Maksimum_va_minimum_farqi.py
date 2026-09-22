import sys


data = list(map(int, sys.stdin.read().split()))
if len(data) > 1:
    n = data[0]
    arr = data[1 : n + 1]
    print(max(arr) - min(arr))