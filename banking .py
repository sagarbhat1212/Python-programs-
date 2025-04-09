def show_balance(balance):
    print("___________________________")    
    print(f"Your balance is ${balance:.2f}")
    print("___________________________")

def Deposit():
    print("___________________________")
    amount = float(input("Enter the amount to deposit: "))
    print("___________________________")
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def Withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be positive")
        return 0
    else:
        return amount

# This is a simple banking program that allows users to check their balance, deposit money, and withdraw money.
# It uses functions to organize the code and make it more readable.

def main():
    balance = 0
    is_running = True 

    while is_running:
         
        print("___________________________")
        print("\nBanking Program")
        print("___________________________")
        
        print("1. Show Balance")
        
        print("2. Show Deposit")
        
        print("3. Withdraw")
        
        print("4. Exit")

        print("___________________________")
        choice = input("Enter your choice (1-4): ")
        print("___________________________")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += Deposit()
        elif choice == "3":
            balance -= Withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("___________________________")
            print("Invalid")
            print("___________________________")
    print("___________________________")
    print("Thank you, have a nice day!")

if __name__ == "__main__":
    main()
