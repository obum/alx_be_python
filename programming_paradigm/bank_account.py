class BankAccount:
    def __init__(self, initial_balance = 0) -> None:
        self.account_balance = round(float(initial_balance), 2)
        
    def deposit(self, amount):
        self.account_balance += amount
        
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')