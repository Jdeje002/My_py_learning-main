## banking app

def banking_intro():
    print("""
    Banking App
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1. Create an account
    2. Deposit
    3. Withdraw
    4. Check balance
    5. Exit
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    choice = int(input("What would you like to do? "))
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        print("Goodbye.")
        exit()
    else:
        print("Invalid choice.")
        banking_intro()

def deposit():
    print("How much would you like to deposit?")
    deposit_amount = int(input("$"))
    global balance
    balance += deposit_amount
    print("Your new balance is " + str(balance))
    banking_intro()
def withdraw():
    print("How much would you like to withdraw?")
    withdraw_amount = int(input("$"))
    global balance
    balance -= withdraw_amount
    print("Your new balance is " + str(balance))
    banking_intro()
def check_balance():
    print("Your current balance is " + str(balance))
    banking_intro()
def create_account():
    print("How much would you like to deposit?")
    deposit_amount = int(input("$"))
    global balance
    balance += deposit_amount
    print("Your new balance is " + str(balance))
    banking_intro()
