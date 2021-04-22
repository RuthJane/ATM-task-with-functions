import random

accountBalance = 0
database = {}

def welcome():
    print("Welcome to RJ Bank")

    own_account = int(input("Do you have account with us ? Press 1 if YES, Press 2 if NO.\n"))

    if own_account == 1:
        login()
    elif own_account == 2:
        print(register())
    else:
        print("Invalid Entry...")

def generate_account_number():
    account_num = random.randrange(0000000000, 9999999999)
    return account_num

def login():
    print("<<<<< Login >>>>>")
    print(generate_account_number())

    user_acct_num = int(input("Enter your account number.\n"))
    user_password = input("Enter your password in letters.\n")

    for accountNumber, userDetails in database.items():
        if accountNumber == user_acct_num:
            if userDetails[3] == user_password:
                bank_operations(user)

    print("Invalid account number or password")
    login()

def register():
    user_register = int(input("Would you like to register with our bank ? Press 1 if YES, Press 2 if NO.\n"))
    print("\n\tGreat!\n\tProceed to register...\t")
    if user_register == 1:

        print("\n- - - Register - - -\n")

        email = input("Enter your email address.\n")
        first_name = input("Enter your first name.\n")
        last_name = input("Enter your last name.\n")
        user_password = input("Enter your password.\n")

        account_num = generate_account_number()

        database[account_num] = [email, first_name, last_name, user_password]
        account_created()

    elif user_register == 2:
        welcome()
    else:
        print("You have entered an invalid option. Try again...")
        register()

def account_created():
    print("Your account has been created.")
    print("===== ===== ===== =====")
    print("Your account number is {} ".format(account_num))
    print("Keep your account number safe.")
    print("===== ===== ===== =====")

    login()

def bank_operations(user):
    print("Welcome, {} {} ".format(user[1], user[2]))

    selected_option = int(input(
        "What bank operations would you want to do ?\n\tPress (1) to Withdraw \n\tPress (2) to Deposit \n\tPress (3) for Complaint \n\tPress (4) to Logout \n\tPress"))

    if selected_option == 1:
        withdraw()
    elif selected_option == 2:
        deposit()
    elif selected_option == 3:
        user_complaint()
    elif selected_option == 4:
        logout()
    else:
        print("Sorry, Invalid Entry. Try again..")
        bank_operations(user)

def withdraw():
    withdrawalAmount = float(input("How much would you like to withdraw? "))
    if withdrawalAmount <= accountBalance:
        accountBalance -= withdrawalAmount
        print("\nProcessing request...")
        print("\nYou have made a withdrawal of #{} ".format(withdrawalAmount))
        print("Take your cash.")
        print("Your balance is #{} ".format(accountBalance))
    else:
        print("\nInsufficient fund. You should make a deposit.")
        bank_operations()

def deposit():
    deposit_amount = float(input("\nHow much do you want to deposit ? "))

    accountBalance += deposit_amount
    print("\nYou have deposited #{} ".format(deposit_amount))
    print("\nYour current balance is #{} ".format(accountBalance))
    logout()

def user_complaint():
    complaint = input("\nWhat issue will you like to report? ")
    print(complaint)
    print("\nWe shall look into it. Thank you for contacting us.")
    logout()

def logout():
    what_else = input("Do you want to do more transaction or logout ? Press 1 if More Transaction or 2 if Exit.\n ")
    if what_else == 1:
        print("Proceed to Login")
        print("==== ==== ==== ====")
        login()
    else:
        print("Goodbye!")
        exit()

welcome()
