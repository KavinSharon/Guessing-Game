import random
print("Guessing Game")
print("Guess Any Number btw 1&9")
number = random.randint(1,9)
chances = 0
while chances<5:
    user = int(input("Enter Your Guess"))
    if number == user:
        print("Congratulations you Are Right")
        break
    elif number<user:
        print("Guess a Smaller Number")
    else:    
        print("Guess a Bigger Number")
    chances = chances+1
if not chances<5:
    print("You Have Lost The Game, The Number Is",number)
            
