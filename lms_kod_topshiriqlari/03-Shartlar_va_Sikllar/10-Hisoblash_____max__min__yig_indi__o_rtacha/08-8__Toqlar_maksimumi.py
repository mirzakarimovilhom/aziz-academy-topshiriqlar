import sys


o = [x for x in map(int, sys.stdin.read().split()[1:]) if x % 2]
print(max(o) if o else "No")