import sys


n, m, x = map(int, sys.stdin.read().split())
print("Yes" if any(x % i == 0 and 1 <= x // i <= m for i in range(1, n + 1)) else "No")