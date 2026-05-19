class Account:
    """Class to represent a bank account"""
    
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Return current balance"""
        return self.balance
    
    def modify(self, name=None, account_type=None):
        """Modify account details"""
        if name:
            self.name = name
        if account_type:
            self.account_type = account_type
    
    def to_dict(self):
        """Convert account to dictionary for web display"""
        return {
            'account_number': self.account_number,
            'name': self.name,
            'account_type': self.account_type,
            'balance': self.balance
        }
    
    def __str__(self):
        """String representation of account"""
        return f"{self.account_number},{self.name},{self.account_type},{self.balance}"
    
    @staticmethod
    def from_string(data_string):
        """Create Account object from string"""
        parts = data_string.strip().split(',')
        return Account(parts[0], parts[1], parts[2], float(parts[3]))
