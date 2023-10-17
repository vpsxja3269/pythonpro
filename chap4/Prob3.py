import random

print("\t\tWelcome to 'Guess My Number'!\n")

print("I'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as possible.\n")

Num = random.randrange(1,101)

Count = 0

while True:
    My_num = int(input("Take a guess: "))
    
    Count += 1
    
    if My_num > Num : 
        print("Lower...")
    
    elif My_num < Num : 
        print("Higher...")
    
    elif My_num == Num :
        print("You guessed it!  The number was", Num)
        print("And it only took you",Count,"tries!")
        
        break

print("\n\n\nPress the enter key to quit.")