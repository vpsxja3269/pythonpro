try:
    num = float(input("Enter a number: "))
except ValueError:
    print("Something went wrong!")

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")

for value in (None, "Hi!"):
    try:
        
        print("Attempting to convert", value, "–>")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")

for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "–>")
        print(float(value))
    except TypeError:
        print("I Can only convert a string or a number!")
    except ValueError:
        print("I Can only convert a string of digits!")

try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("Not a number! Or as Python would say:\n", e)

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)