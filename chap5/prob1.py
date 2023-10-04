items = ("sword", "armor", "shield", "healing potion")
chest = ("gold", "gems")

print("your items")
for v in items:
    print(v)

print("\nPress the enter key to continue.")
print("You have ",len(items)," items in your possenssion.\n")

print("Press the enter key to continue.")
if "healing potin" in items:
    print("You will live to fight another day.")
else :
    print("You don't have Helling potion")

items_index = int(input("Enter the index number for an item in inventory: "))
print("At index ",items_index, "is ", items[items_index])

bigin = int(input("Enter the index number to begin a slice : "))
end = int(input("Enter the index number to end the slice : "))
print("inventory[ ",bigin," : ",end," ]\t\t<",items[bigin:end],">\n")

print("Press the enter key to continue.")
print("You find a chest. It contains:")
print("<",chest,">")
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
items += chest
print("<",items,">")
