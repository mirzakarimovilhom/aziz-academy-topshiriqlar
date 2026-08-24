import sys 


s = list(map(int, sys.stdin.read().split()))
print(s.index(next(x for x in s if x < 0)))