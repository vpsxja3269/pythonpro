Word = {"404":"clueless", "Unintalled" : "being fired."}

while True :
    print("\n\tGeek Translator\n")
    print("\t0 - Quit")
    print("\t1 - Look Up a Geek Term")
    print("\t2 - Add a Geek Term")
    print("\t3 - Redefine a Geek Term")
    print("\t4 - Delete a Geek Term")
    print("\t5 - Words in the dictionary\n")
    num = int(input("Choice : "))

    if num == 0 :
        break

    elif num == 1 :
        find = input("What term  do you want me to translate?: ")

        if find in Word:
            print(find, "means", Word[find])
        
        else:
            print("I have no idea what", find, "is.")
    
    elif num == 2 :
        add = input("Enter characters to add: ")
       
        if add in Word:
            print("Already exists")
       
        else :
            means = input("Enter the meaning of the characters: ")
            Word[add] = means
    
    elif num == 3 :
        reply = input("Enter the character you want to redefine: ")
        
        if reply in Word:
            remeans = input("Meaning of character to override: ")
            Word[reply] = remeans
        
        else :
            print("It does not exist.\n")
    
    elif num == 4 :
        delchr = input("Enter the word you want to delete: ")
        
        if delchr in Word:
            print("Deleted successfully.")
            del Word[delchr]
       
        else :
            print("That word doesn't exist")
    
    elif num == 5 :
        print("\nWords registered in the dictionary>> ",end='')
     
        for key, value in Word.items():
            print("[",key,"]", end = ' ')
        print("\n")