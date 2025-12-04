# ATM Simulation (Brainwave Matrix Intern Project)

This is a simple console-based ATM simulation application developed as part of the Brainwave Matrix internship.  
It demonstrates core Python concepts such as object-oriented programming, input handling, and basic validation.

## Features

- PIN authentication before accessing the ATM
- Check current account balance
- Deposit money with validation for positive amounts
- Withdraw money with sufficient balance check
- User-friendly text menu loop with exit option
- Basic error handling for invalid numeric inputs

## How It Works

- The `ATM` class stores the user PIN and balance.
- The user is prompted to enter a PIN; access is granted only if it matches.
- A menu is displayed repeatedly until the user chooses to exit.
- For each choice, the corresponding method is called:
  - `check_balance()` to display the current balance
  - `deposit(amount)` to add funds
  - `withdraw(amount)` to remove funds safely

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP) concepts
- Console-based input/output

## File Structure

- `atm_project.py` – Main Python script containing:
  - `ATM` class definition
  - `main()` function
  - Entry point `if __name__ == "__main__": main()`

## How to Run

1. Make sure Python 3 is installed on your system.
2. Save the file as `atm_project.py`.
3. Open a terminal or command prompt in the project folder.
4. Run the script with:


5. Enter the PIN when prompted (default in the code: `1234`), then use the menu to interact with the ATM.

## Possible Improvements

- Support for multiple user accounts
- Transaction history (mini statement)
- Saving and loading balance from a file or database
- GUI or web-based interface in the future
