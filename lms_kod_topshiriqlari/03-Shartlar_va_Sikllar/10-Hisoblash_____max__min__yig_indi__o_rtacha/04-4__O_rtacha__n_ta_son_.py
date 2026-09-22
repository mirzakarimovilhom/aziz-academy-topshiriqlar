import sys
 
    
data = list(map(int, sys.stdin.read().split()))
n = data[0]
arr = data[1 : n + 1]
print(sum(arr) / len(arr))