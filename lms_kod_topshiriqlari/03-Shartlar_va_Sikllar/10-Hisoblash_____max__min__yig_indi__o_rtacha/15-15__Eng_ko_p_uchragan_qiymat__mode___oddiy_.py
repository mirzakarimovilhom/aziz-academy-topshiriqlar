import sys


data = sys.stdin.read().split()[1:]
print(max(set(data), key=lambda x: (data.count(x), -int(x))))