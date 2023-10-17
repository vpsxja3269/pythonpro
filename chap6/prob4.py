import random

Word = ["python","hangman","game"]
R_word = list(random.choice(Word))
chrarr = []

OX = False

Emp_R_Word = ["_" for i in range(len(R_word))]

hangman = [["_______"],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|      "],
           ["|_______"]]

cnt = 0

while True:
    print("\n")
    chr = input("Enter your guess: ")
    chrarr.append(chr)
    print("\n")
    
    for i in range(len(R_word)):
        if(R_word[i] == chr):
            Emp_R_Word[i] = chr
            OX = True

    if OX == True:
        print("Yes!",chr,"is in the word!")
        OX = False

    else :
        print("No!",chr,"is not in the word!")
        cnt+=1
    
    if cnt == 1:
        hangman[1]=["|    | "]

    elif cnt == 2:
        hangman[2]=["|    O "]

    elif cnt == 3:
        hangman[3]=["|    + "]

    elif cnt == 4:
        hangman[3]=["|   -+-"]

    elif cnt == 5:
        hangman[4]=["|    | "]

    elif cnt == 6:
        hangman[5]=["|   /| "]

    elif cnt == 7:
        hangman[6]=["|  / | "]

    for i in range(len(hangman)):
            print(hangman[i])

    if cnt == 7 :
        print("\nGame Over!")
        break
    
    print("\n\n")
    print("You've used the following letters:")
    print(chrarr)
    print("\n")
    print("Currently entered word: ")

    for i in range(len(Emp_R_Word)):
        print(Emp_R_Word[i],end=' ')

    print("\n\n")

    if(Emp_R_Word == R_word):
        print("Success.")
        break


    