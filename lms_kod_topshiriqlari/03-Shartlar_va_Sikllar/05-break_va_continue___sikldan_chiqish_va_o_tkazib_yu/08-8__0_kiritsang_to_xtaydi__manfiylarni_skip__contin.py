total = 0


while True:
    num = int(input())
    if num == 0:
        break
    if num < 0:
        continue
    total += num 
    
    
print(total)