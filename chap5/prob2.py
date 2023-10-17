import random

Word = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")

print("Welcome to word Jumble!\n Unscramble the letters to make a word.")

Jumble = random.choice(Word)
x = list(Jumble)
random.shuffle(x)

print("Jumble word : ",end='')
for i in range(len(x)):
    print(x[i],end='')

print("\n")

guess = input("Your guess : ")
if Jumble == guess:
    print("good Man~")
else:
    print("Sorry, that's not correct. The word was : ", end = "")

    for i in range(len(Jumble)) :
        print(Jumble[i], end= "")
