import sys


total = 0
for line in sys.stdin:
    num = int(line.strip())
    if num % 2 != 0:
        break
    total += num
    
    
print(total)