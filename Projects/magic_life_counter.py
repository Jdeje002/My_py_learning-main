###


### starting damage 40
### starting commander damage 21
### starting infect damage 15

import time


starting_health = 40
starting_commander_health = 21
starting_infect = 15



def commander_menu():
    print("""
    1. Life Damage
    2. Commander Damage
    3. Infect Damage
    4. Exit
    """)
    choice = int(input("What would you like to do? "))
    if choice == 1:
        life_damage(int(input("How much damage? ")))
    elif choice == 2:
        commander_damage(int(input("How much Commander damage? ")))        
    elif choice == 3:
        infect_damage(int(input("How much infect damage? ")))
    elif choice == 4:
        print("Goodbye.")
    else:
        print("Invalid choice.")
        commander_menu()


def commander_intro():
    print("""
    Magic The Gathering Life Counter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Your starting health is 40.
    Your starting commander health is 21.
    Your starting infect is 15.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    commander_menu()

def health_status():
    print("\n")
    print("Your health is " + str(starting_health))
    print("Your commander health is " + str(starting_commander_health))
    print("Your infect is " + str(starting_infect))
    time.sleep(1)
    print("\n")

def life_damage(x):
    global starting_health
    starting_health -= x
    if starting_health <= 0:
        print("You died!")
        exit()
    else:
        health_status()
        commander_menu()

def commander_damage(x):
    global starting_commander_health
    starting_commander_health -= x
    if starting_commander_health <= 0:
        print("You died!")
        exit()
    else:
        health_status()
        commander_menu()

def infect_damage(x):
    global starting_infect
    starting_infect -= x
    if starting_infect <= 0:
            print("You died!")
            exit()
    else:
        health_status()
        commander_menu()


commander_intro()
