target = 5
attempts = 0


while attempts < 3:
    guess = int(input())
    attempts += 1
    if guess == target:
        print("Correct")
        break
                                 
else:    
    print("Game Over")