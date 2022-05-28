## dice roller for DND

import random 

## dice roller

d_6 = random.randint(1,6)
d_10 = random.randint(1,10)
d_20 = random.randint(1,20)
d_100 = random.randint(1,100)


def dice_menu():
    print("""   Dice Roller
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1. d6
    2. d10
    3. d20
    4. d100
    5. Quit
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

def roll_dice():
    dice_menu()
    choice = input("What dice would you like to roll? ")
    if choice == "1":
        print("You rolled a " + str(d_6))
        dice_menu()
    elif choice == "2":
        print("You rolled a " + str(d_10))
        dice_menu()
    elif choice == "3":
        print("You rolled a " + str(d_20))
        dice_menu()
    elif choice == "4":
        print("You rolled a " + str(d_100))
        dice_menu()
    elif choice == "5":
        print("Goodbye.")
        exit()
    else:
        print("Invalid choice.")
        dice_menu()


