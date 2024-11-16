class Account:
    """
    Represents a user's bank account with basic functionalities
    for balance verification and withdrawal.
    """
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        """
        Returns the current account balance.
        """
        return self.balance

    def deduct_amount(self, amount):
        """
        Deducts the requested amount from the account balance
        if sufficient funds are available. Otherwise, raises an error.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount % 100 != 0:
            raise ValueError("Amount must be in multiples of $100.")
        self.balance -= amount
        return amount


class ATM:
    """
    Simulates an ATM machine for withdrawing cash from an account.
    """
    def __init__(self, location, branch_name):
        self.location = location
        self.branch_name = branch_name

    def withdraw_cash(self, account, amount):
        """
        Handles the withdrawal process: checks balance, deducts amount,
        and simulates cash dispensing.
        """
        try:
            print(f"Processing withdrawal request for ${amount}...")
            withdrawn_amount = account.deduct_amount(amount)
            print(f"Success! ${withdrawn_amount} has been withdrawn.")
            print(f"Remaining balance: ${account.check_balance()}.")
            print("Please take your cash.")
        except ValueError as e:
            print(f"Transaction failed: {e}")


# Example Usage
if __name__ == "__main__":
    # Initialize the ATM and an account
    atm = ATM("Downtown", "Main Branch")
    user_account = Account(account_number="123456789", balance=1000)

    print(f"Welcome to {atm.branch_name} ATM at {atm.location}!")
    print(f"Current balance: ${user_account.check_balance()}.")

    # Perform a withdrawal
    amount_to_withdraw = 300  # Modify this value to test different scenarios
    atm.withdraw_cash(user_account, amount_to_withdraw)
