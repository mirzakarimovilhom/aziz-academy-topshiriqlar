import sys


print(*[x for x in sys.stdin.read().split()[1:] if  int(x) % 5 == 0], sep="\n")