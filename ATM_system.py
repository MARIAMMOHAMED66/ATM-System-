# Define the ATM class to display location and branch name
class ATM:
    def __init__(self, location, branch_name):
        self.location = location
        self.branch_name = branch_name

    def Show(self):
        print(f"ATM Location: {self.location}")
        print(f"ATM Branch: {self.branch_name}")

# Define the Account class to manage user accounts with withdrawal functionality
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Transaction successful. You have withdrawn {amount}.")
            print(f"Remaining balance: {self.balance}")

# Define the ATMInterface class to represent the ATM user interface
class ATMInterface:
    def __init__(self, atm, account):
        self.atm = atm
        self.account = account

    def display(self):
        # Display location and branch name
        self.atm.Show()
        
        # Get the withdrawal amount from the user
        try:
            amount = float(input("Enter the amount you wish to withdraw: "))
            # Attempt to withdraw the amount
            self.account.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# The code that ties all classes together
if __name__ == "__main__":
    # Create instances of the different classes
    atm = ATM("Main Branch", "InfoSuper Bank")  # Set ATM location and branch name
    account = Account(1000)  # Create an account with a balance of 1000
    atm_interface = ATMInterface(atm, account)  # Link the ATM to the account

    # Display the ATM interface and start the process
    atm_interface.display()

