class BankAccount:
    bank_name = "GDGOC Bank"
    account_count = 0
    
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transaction_history = []
        
        BankAccount.account_count += 1
        
        if initial_balance > 0:
            self.__transaction_history.append(f"Initial deposit: ${initial_balance:.2f}")
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return False
        
        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"Insufficient funds! Current balance: ${self.__balance:.2f}")
            return False
        
        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawal: -${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        return True
    
    def get_transaction_history(self):
        return self.__transaction_history.copy()
    
    def display_info(self):
        print(f"\n{'='*50}")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ${self.__balance:.2f}")
        print(f"{'='*50}\n")
    
    def __str__(self):
        return f"BankAccount({self.__account_holder}, {self.__account_number}, ${self.__balance:.2f})"
    
    def __repr__(self):
        return f"BankAccount('{self.__account_holder}', '{self.__account_number}', {self.__balance})"
    
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.__account_number == other.__account_number
        return False
    
    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance < other.__balance
        return NotImplemented
    
    def __add__(self, amount):
        if isinstance(amount, (int, float)):
            self.deposit(amount)
        return self
    
    def __sub__(self, amount):
        if isinstance(amount, (int, float)):
            self.withdraw(amount)
        return self


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, initial_balance=0, interest_rate=0.03):
        super().__init__(account_holder, account_number, initial_balance)
        self.__interest_rate = interest_rate
    
    def get_interest_rate(self):
        return self.__interest_rate
    
    def apply_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Interest applied: ${interest:.2f} at {self.__interest_rate*100}% rate")
    
    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.__interest_rate*100}%")
        print(f"{'='*50}\n")
    
    def __str__(self):
        return f"SavingsAccount({self.get_account_holder()}, ${self.get_balance():.2f}, {self.__interest_rate*100}%)"


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, account_number, initial_balance=0, overdraft_limit=500):
        super().__init__(account_holder, account_number, initial_balance)
        self.__overdraft_limit = overdraft_limit
    
    def get_overdraft_limit(self):
        return self.__overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        available = self.get_balance() + self.__overdraft_limit
        
        if amount > available:
            print(f"Exceeds overdraft limit! Available: ${available:.2f}")
            return False
        
        new_balance = self.get_balance() - amount
        
        if new_balance < 0:
            print(f"⚠ Using overdraft: ${abs(new_balance):.2f}")
        
        return super().withdraw(amount)
    
    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: ${self.__overdraft_limit:.2f}")
        print(f"{'='*50}\n")
    
    def __str__(self):
        return f"CheckingAccount({self.get_account_holder()}, ${self.get_balance():.2f}, OD: ${self.__overdraft_limit})"


class PremiumAccount(SavingsAccount):
    def __init__(self, account_holder, account_number, initial_balance=0):
        super().__init__(account_holder, account_number, initial_balance, interest_rate=0.05)
        self.__reward_points = 0
    
    def deposit(self, amount):
        if super().deposit(amount):
            points = int(amount / 10)
            self.__reward_points += points
            if points > 0:
                print(f"Earned {points} reward points!")
            return True
        return False
    
    def get_reward_points(self):
        return self.__reward_points
    
    def redeem_points(self, points):
        if points > self.__reward_points:
            print(f"Insufficient points! You have {self.__reward_points} points.")
            return False
        
        cash_value = points / 100
        self.__reward_points -= points
        self.deposit(cash_value)
        print(f"Redeemed {points} points for ${cash_value:.2f}")
        return True
    
    def display_info(self):
        super().display_info()
        print(f"Reward Points: {self.__reward_points}")
        print(f"{'='*50}\n")
    
    def __str__(self):
        return f"PremiumAccount({self.get_account_holder()}, ${self.get_balance():.2f}, Points: {self.__reward_points})"


def demonstrate_oop_concepts():
    print("="*60)
    print("BANK ACCOUNT SYSTEM - OOP DEMONSTRATION")
    print("="*60)
    
    print("\nCreating Basic Account:")
    acc1 = BankAccount("Hammad Ali", "ACC001", 1000)
    acc1.display_info()
    
    print("\nDeposit and Withdraw Operations:")
    acc1.deposit(500)
    acc1.withdraw(200)
    
    print("\nMagic Methods:")
    print(f"String representation: {acc1}")
    print(f"Official representation: {repr(acc1)}")
    
    print("\nUsing Operators (Magic Methods):")
    acc1 + 100
    acc1 - 50
    
    print("\nSavings Account (Inheritance):")
    savings = SavingsAccount("Sara Khan", "SAV001", 5000, 0.04)
    savings.display_info()
    savings.apply_interest()
    
    print("\nChecking Account (Polymorphism):")
    checking = CheckingAccount("Ahmed Hassan", "CHK001", 1000, 500)
    checking.display_info()
    checking.withdraw(1200)
    
    print("\nPremium Account:")
    premium = PremiumAccount("Hammad Ali", "PREM001", 10000)
    premium.display_info()
    premium.deposit(500)
    premium.deposit(1000)
    print(f"Total reward points: {premium.get_reward_points()}")
    premium.redeem_points(100)
    
    print("\nAccount Comparison:")
    acc2 = BankAccount("John Doe", "ACC002", 2000)
    print(f"acc1 balance: ${acc1.get_balance():.2f}")
    print(f"acc2 balance: ${acc2.get_balance():.2f}")
    print(f"acc1 < acc2: {acc1 < acc2}")
    
    print("\nTransaction History:")
    print(f"Account: {acc1.get_account_holder()}")
    for transaction in acc1.get_transaction_history():
        print(f"  • {transaction}")
    
    print("\nClass Variables:")
    print(f"Bank Name: {BankAccount.bank_name}")
    print(f"Total Accounts Created: {BankAccount.account_count}")
    
    print("\n" + "="*60)
    print("OOP Demonstration Complete!")
    print("="*60)


if __name__ == "__main__":
    demonstrate_oop_concepts()
