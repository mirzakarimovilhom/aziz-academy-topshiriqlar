import sys


n = int(sys.stdin.read().strip())
print(sum(i * j for i in range(1, n + 1) for j in range(1, n + 1)))
      