import random
print('I sense your energy. Your true emotion are coming across my screen.')

emotion = random.randrange(1,4)

if emotion == 1:
    print("-----------")
    print("|   0 0   |")
    print("|    <    |")
    print("| \     / |")
    print("|  \   /  |")
    print("|   \ /   |")
    print("|    _    |")
    print("|         |")
    print("-----------")

elif emotion == 2:
    print("-----------")
    print("|   0 0   |")
    print("|    _    |")
    print("|         |")
    print("-----------")

elif emotion == 3:
    print("-----------")
    print("|   0 0   |")
    print("|    <    |")
    print("|    _    |")
    print("|   / \   |")
    print("|  /   \  |")
    print("-----------")

