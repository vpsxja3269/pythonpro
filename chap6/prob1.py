item = ["sword", "armor", "shield", "healing potion"]

print("Your items : ")

for i in range(len(item)):
        print(item[i])

print("\nPress the enter key to continue.")
print("You have",len(item),"items in your possession.\n")

print("Press the enter key to continue.")
print("You will live to fight another day.\n")

num = int(input("Enter the index number for an item in inventory: "))
print("At index",num,"is",item[num],"\n")

sli1 = int(input("Enter the index number to begin a slice : "))
sli2 = int(input("Enter the index number to end the slice : "))
print("inventory[",sli1,":",sli2,"]\t\t",item[sli1:sli2],"\n")

print("Press the enter key to continue.")
print("You find a chest which contains:")
chest = ["gold","gems"]
print(chest)
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
item += chest
print(item)
print("\nPress the enter key to continue.")

print("\nYou trade your sword for a crossbow.")
print("Your inventroy is now:")
item[0] = "crossbow"
print(item)
print("\nPress the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
print("Your inventory is now:")
item[4:6] = ["orb of future telling"]
print(item)

print("\nPress the enter key to continue.")
print("In a great battle, your shield is destroyed.")
print("Your inventory is now:")
item.remove("shield")
print(item)

print("\nPress the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")
print("Your inventory is now:")
item.remove("crossbow")
item.remove("armor")
print(item)

print("\n\nPress the enter key to exit.")