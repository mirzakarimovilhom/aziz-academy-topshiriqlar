import sys 


print(*[x for x in sys.stdin.read().split()[1:] if int(x) < 0], sep="\n")