class ATM:
    def _init_(self, user_pin, user_balance=0):
        self.pin = user_pin
        self.balance = user_balance

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def display_menu(self):
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        print(f"Your balance is ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")


def main():
    atm = ATM(user_pin="1234", user_balance=1000.00)  # You can modify this starting balance and PIN

    print("Welcome to the ATM")
    entered_pin = input("Enter your PIN: ")

    if not atm.check_pin(entered_pin):
        print("Incorrect PIN. Exiting...")
        return

    while True:
        atm.display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Try again.")


if _name_ == "_main_":
    main()