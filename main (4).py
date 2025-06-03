class BankAccount:
    def _init_(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Enter a valid amount to withdraw.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def exit(self):
        print("Thank you for banking with us. Goodbye!")
# Menu-driven interface
def main():
    print("=== Welcome to Python Bank ===")
    name = input("Enter your name to create an account: ")
    account = BankAccount(account_holder=name)
    while True:
        print("\nPlease choose an option:")
        print("1. Deposit Money")
        print("")