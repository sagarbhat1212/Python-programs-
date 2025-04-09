import random

def spin_row():
    symbols = ["🍒", "🍉", "⭐️", "🍋", "🔔"]
    result = [random.choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print("____________________________")
    print(" | ".join(row))
    print("____________________________")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 10
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "⭐️":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 2
        elif row[0] == "🔔":
            return bet * 1
    return 0  # No match

def main():
    balance = 100

    print("____________________________")
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍉 ⭐️ 🍋 🔔")
    print("____________________________")

    while balance > 0:
        print(f"Your balance is: ${balance:.2f}")
        bet = input("Enter your bet amount: $")

        if not bet.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Invalid bet amount. Please enter a positive number.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning ....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 Congratulations! You won ${payout:.2f}!")
            balance += payout
        else:
            print("😞 Sorry, you lost this round.")
        
        print("____________________________")

    print("You are out of money! Game over.")
    print("____________________________")
    print("Thanks for playing!")
    print("____________________________")

if __name__ == "__main__":
    main()
