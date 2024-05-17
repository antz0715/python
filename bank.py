def display_menu():
    print("Banking System Menu:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Quit")

def check_balance(account):
    print(f"Your balance is: ${account['balance']}")

def deposit_money(account):
    amount = float(input("Enter amount to deposit: "))
    account['balance'] += amount
    print(f"${amount} deposited. New balance: ${account['balance']}")

def withdraw_money(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount > account['balance']:
        print("Insufficient funds.")
    else:
        account['balance'] -= amount
        print(f"${amount} withdrawn. New balance: ${account['balance']}")

def banking_system():
    account = {'balance': 0.0}
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            check_balance(account)
        elif choice == '2':
            deposit_money(account)
        elif choice == '3':
            withdraw_money(account)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

banking_system()
