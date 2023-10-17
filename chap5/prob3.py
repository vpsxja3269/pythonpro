import random

Word = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
a = False
b = False

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")

rword = random.choice(Word)
cnt = len(rword)
guessword = ["_" for i in range(cnt)]

print(guessword)
print("Length of the selected word:",cnt)
print(rword)

while True:
   if cnt == 0 : break

   print("Remaining attemps:",cnt)
   print("Current guessed word: ",end = '')
   print("I Love You")
   
   for i in range(len(rword)):
       print(guessword[i],end=' ')
       print()
   
   inguess = input("Guess a letter: ")

   for i in range(len(rword)):
       if(inguess == rword[i]):
           guessword[i] = inguess
           a = True
   
   if a != True:
       cnt -= 1
   
   a = False
    
   if "_" in guessword:
        continue
   
   else :
      b = True
      print("Congratulations! You guessed the word:",rword)
      break

if b == False : 
    print("Incorrect guess.\n")
    print("You've used up all your attempts. The correct ord was python.")