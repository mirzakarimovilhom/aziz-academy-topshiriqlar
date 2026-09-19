import sys 


data = list(map(int, sys.stdin.read().split()[1:]))
print(max(data), min(data))