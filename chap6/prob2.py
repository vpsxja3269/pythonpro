List = {}
Name = []

while True:
    print("\tHigh Scores Keeper")
    print("\n\t0 - Quit")
    print("\t1 - List Scores")
    print("\t2 - Add a Score")
    print("\n")

    num = int(input("Choice: "))

    if num == 0 :
        break

    elif num == 1 :
        print("\nHigh Scores\n")
        print("NAME\tSCORE")

        for i in range(len(Name)):
            print(Name[i],"\t",List.get(Name[i]))
            
        print("\n")

    elif num == 2 :
        print("\n")
        Name_Add = input("What is the player's name?: ")
        Name.append(Name_Add)
        addscore = input("What score did the player get? : ")
        List[Name_Add] = addscore