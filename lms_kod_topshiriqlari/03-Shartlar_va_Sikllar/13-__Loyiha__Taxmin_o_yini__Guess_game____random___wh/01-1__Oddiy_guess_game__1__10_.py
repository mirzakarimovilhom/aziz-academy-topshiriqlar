target = 7


while True:
    guess = int(input())
    if guess < target:
        print("Low")
    elif guess > target:
        print("High")
    else:
        print("Correct")
        break