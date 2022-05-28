## dice roller for DND

import random
from tkinter import Menu 

## dice roller



def roll_d_4():
    print("You rolled a " + str(random.randint(1,4)))
    print("\n")
    dice_menu()
def roll_d_6():
    print("You rolled a " + str(random.randint(1,6)))
    print("\n")
    dice_menu()
def roll_d_10():
    print("You rolled a " + str(random.randint(1,10)))
    print("\n")
    dice_menu()
def roll_d_20():
    roll = random.randint(1,20)
    if roll == 20:
        print("Critical Hit!")
        print("You rolled a " + str(roll))
    elif roll == 1:
        print("Critical Miss!")
        print("You rolled a " + str(roll))
    else:
        print("You rolled a " + str(roll))
    print("\n")
    dice_menu()
def roll_d_100():
    print("You rolled a " + str(random.randint(1,100)))
    print("\n")
    dice_menu()


def dice_menu():
    print("""   
    Dice Roller
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1. Roll a d4
    2. Roll a d6
    3. Roll a d10
    4. Roll a d20
    5. Roll a d100
    6. Exit
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    choice = int(input("What dice would you like to roll? "))
    roll_dice(choice)

def roll_dice(x):
    if x == 1:
        roll_d_4()
      
    elif x == 2:
        roll_d_6()
       
    elif x == 3:
        roll_d_10()
       
    elif x == 4:
        roll_d_20()
       
    elif x == 5:
        roll_d_100()
       
    elif x == 6:
        print("Goodbye.")
        exit()
    else:
        print("Invalid choice.")
        dice_menu()

dice_menu()
