import os
from bank_account import Account

class BankOperations:
    """Class to handle all bank operations"""
    
    def __init__(self, filename="accounts.dat"):
        self.filename = filename
        self.accounts = {}
        self.load_accounts()
    
    def load_accounts(self):
        """Load accounts from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    for line in file:
                        if line.strip():
                            account = Account.from_string(line)
                            self.accounts[account.account_number] = account
            except Exception as e:
                print(f"Error loading accounts: {e}")
    
    def save_accounts(self):
        """Save all accounts to file"""
        try:
            with open(self.filename, 'w') as file:
                for account in self.accounts.values():
                    file.write(str(account) + '\n')
            return True
        except Exception as e:
            print(f"Error saving accounts: {e}")
            return False
    
    def create_account(self, account_number, name, account_type, initial_deposit=0):
        """Create a new account"""
        if account_number in self.accounts:
            return False, "Account number already exists!"
        
        if initial_deposit < 0:
            return False, "Initial deposit cannot be negative!"
        
        new_account = Account(account_number, name, account_type, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_accounts()
        return True, "Account created successfully!"
    
    def deposit_money(self, account_number, amount):
        """Deposit money to an account"""
        if account_number not in self.accounts:
            return False, "Account not found!"
        
        if amount <= 0:
            return False, "Amount must be positive!"
        
        account = self.accounts[account_number]
        account.deposit(amount)
        self.save_accounts()
        return True, f"₹{amount:.2f} deposited successfully! New balance: ₹{account.get_balance():.2f}"
    
    def withdraw_money(self, account_number, amount):
        """Withdraw money from an account"""
        if account_number not in self.accounts:
            return False, "Account not found!"
        
        if amount <= 0:
            return False, "Amount must be positive!"
        
        account = self.accounts[account_number]
        if account.get_balance() < amount:
            return False, f"Insufficient balance! Current balance: ₹{account.get_balance():.2f}"
        
        account.withdraw(amount)
        self.save_accounts()
        return True, f"₹{amount:.2f} withdrawn successfully! New balance: ₹{account.get_balance():.2f}"
    
    def check_balance(self, account_number):
        """Check account balance"""
        if account_number not in self.accounts:
            return False, "Account not found!", None
        
        account = self.accounts[account_number]
        return True, f"Current balance: ₹{account.get_balance():.2f}", account.to_dict()
    
    def get_account(self, account_number):
        """Get account details"""
        if account_number not in self.accounts:
            return None
        return self.accounts[account_number]
    
    def modify_account(self, account_number, name=None, account_type=None):
        """Modify account details"""
        if account_number not in self.accounts:
            return False, "Account not found!"
        
        account = self.accounts[account_number]
        account.modify(name, account_type)
        self.save_accounts()
        return True, "Account modified successfully!"
    
    def close_account(self, account_number):
        """Close an account"""
        if account_number not in self.accounts:
            return False, "Account not found!"
        
        del self.accounts[account_number]
        self.save_accounts()
        return True, "Account closed successfully!"
    
    def get_all_accounts(self):
        """Get all accounts as list of dictionaries"""
        return [account.to_dict() for account in self.accounts.values()]