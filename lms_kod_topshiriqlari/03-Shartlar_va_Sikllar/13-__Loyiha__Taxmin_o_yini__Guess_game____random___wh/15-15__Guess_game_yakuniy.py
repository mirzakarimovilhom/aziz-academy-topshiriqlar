import sys


lines = sys.stdin.read().split()


secret = 20
attempts = 0


for val in lines:
    attempts += 1
    try:
        n = int(val)
    except ValueError:
        print("Invalid")
        continue
        
        
    if n < 1 or n > 20:
        print("Invalid")
    elif n < secret:
        print("Low")
    elif n > secret:
        print("High")
    else:
        print("Correct")
        break
        
        
print(attempts)