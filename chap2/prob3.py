Name = input("What's your name? ")
Age = int(input("And how old are you? "))
Weigh = int(input("Okay, last question. How many pounds do you weigh? "))

age_dog = Age/7
age_seconds = Age * 31536000

print("Did you know that you're just",age_dog, "in dog years?")
print("\nBut you're also over", age_seconds, "seconds old.")

print("\nIf a small child were trying to get your attention, your name would become ", Name, Name, Name, Name, Name, sep="")

moon_weigh = Weigh / 6
sun_weigh = Weigh * 27.1

print("\nDid you know that on the moon you would weigh only", moon_weigh, "pounds?")
print("But on the sun, you'd weigh", sun_weigh, "<but, ah... not for long>.")
print("\nPress the enter key to exit.")