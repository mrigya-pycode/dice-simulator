import random

while True:
    print('Do you want me to roll the dice?')
    answer = input()
    if answer == 'yes' or answer == 'y' or answer == "Y":
        i = random.randint(1,6)
        if i == 1:
            print("-----------")
            print("|         |")
            print("|    0    |")
            print("|         |")
            print("-----------")
        if i == 2:
            print("-----------")
            print("|    0    |")
            print("|         |")
            print("|    0    |")
            print("-----------")
        if i == 3:
            print("-----------")
            print("|    0    |")
            print("|    0    |")
            print("|    0    |")
            print("-----------")
        if i == 4:
            print("-----------")
            print("| 0     0 |")
            print("|         |")
            print("| 0     0 |")
            print("-----------")
        if i == 5:
            print("-----------")
            print("| 0     0 |")
            print("|    0    |")
            print("| 0     0 |")
            print("-----------")
        if i == 6:
            print("-----------")
            print("| 0     0 |")
            print("| 0     0 |")
            print("| 0     0 |")
            print("-----------")

    else:
        exit()



