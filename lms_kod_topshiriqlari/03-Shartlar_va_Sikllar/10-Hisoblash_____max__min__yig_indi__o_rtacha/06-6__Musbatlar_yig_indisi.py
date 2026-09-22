import sys


data = sys.stdin.read().split()
if not data:
    exit()
    
    
n = int(data[0])
a = [int(x) for x in data[1:]]


print(sum(x for x in a if x > 0))