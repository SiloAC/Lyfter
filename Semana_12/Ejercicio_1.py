class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrawal successful. Current balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        BankAccount.__init__(self, balance)  # allows SavingsAccount to have BankAccount's balance
        self.min_balance = min_balance 

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance - amount < self.min_balance:
            print(f"Cannot withdraw {amount}. Balance cannot go below minimum balance of {self.min_balance}.")
            return 
        BankAccount.withdraw(self, amount)


# Create a savings account with balance 1000 and min_balance 200
account = SavingsAccount(balance=1000, min_balance=200)

account.deposit(500)     # Adds 500, new balance: 1500
account.withdraw(1000)   # Withdraws 1000, new balance: 500
account.withdraw(400)    # Fails: would drop below 200
account.withdraw(-50)    # Fails: negative amount