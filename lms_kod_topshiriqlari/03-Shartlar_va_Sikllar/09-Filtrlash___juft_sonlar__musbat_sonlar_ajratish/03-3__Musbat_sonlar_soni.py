import sys


print(sum(1 for x in sys.stdin.read().split()[1:] if int(x) > 0))