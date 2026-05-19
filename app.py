from flask import Flask, render_template, request, redirect, url_for, session
from bank_operations import BankOperations
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_this_to_something_secure'

# Initialize bank operations
bank = BankOperations()

# File to store user credentials
USERS_FILE = "users.dat"

def load_users():
    """Load users from file"""
    users = {}
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as file:
                for line in file:
                    if line.strip():
                        username, password = line.strip().split(',')
                        users[username] = password
        except Exception as e:
            print(f"Error loading users: {e}")
    return users

def save_user(username, password):
    """Save a new user to file"""
    try:
        with open(USERS_FILE, 'a') as file:
            file.write(f"{username},{password}\n")
        return True
    except Exception as e:
        print(f"Error saving user: {e}")
        return False

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', error='Please login first'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    error = request.args.get('error', '')
    success = request.args.get('success', '')
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        users = load_users()
        
        if username in users:
            if users[username] == password:
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('index', success='Login successful'))
            else:
                return render_template('login.html', error='Invalid password')
        else:
            return render_template('login.html', error='Username not found')
    
    return render_template('login.html', error=error, success=success)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page"""
    error = ''
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not username or not password:
            error = 'Username and password are required'
        elif len(username) < 3:
            error = 'Username must be at least 3 characters'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters'
        elif password != confirm_password:
            error = 'Passwords do not match'
        else:
            users = load_users()
            if username in users:
                error = 'Username already exists'
            else:
                if save_user(username, password):
                    return redirect(url_for('login', success='Registration successful! You can now login'))
                else:
                    error = 'Error creating account'
        
        return render_template('register.html', error=error)
    
    return render_template('register.html', error='')

@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    return redirect(url_for('login', success='Logged out successfully'))

@app.route('/')
@login_required
def index():
    """Home page"""
    success = request.args.get('success', '')
    return render_template('index.html', username=session.get('username'), success=success)

@app.route('/create_account', methods=['GET', 'POST'])
@login_required
def create_account():
    """Create new account page"""
    message = ''
    message_type = ''
    
    if request.method == 'POST':
        account_number = request.form.get('account_number')
        name = request.form.get('name')
        account_type = request.form.get('account_type')
        initial_deposit = float(request.form.get('initial_deposit', 0))
        
        success, msg = bank.create_account(account_number, name, account_type, initial_deposit)
        message = msg
        message_type = 'success' if success else 'error'
    
    return render_template('create_account.html', message=message, message_type=message_type)

@app.route('/deposit', methods=['GET', 'POST'])
@login_required
def deposit():
    """Deposit money page"""
    message = ''
    message_type = ''
    
    if request.method == 'POST':
        account_number = request.form.get('account_number')
        amount = float(request.form.get('amount'))
        
        success, msg = bank.deposit_money(account_number, amount)
        message = msg
        message_type = 'success' if success else 'error'
    
    return render_template('deposit.html', message=message, message_type=message_type)

@app.route('/withdraw', methods=['GET', 'POST'])
@login_required
def withdraw():
    """Withdraw money page"""
    message = ''
    message_type = ''
    
    if request.method == 'POST':
        account_number = request.form.get('account_number')
        amount = float(request.form.get('amount'))
        
        success, msg = bank.withdraw_money(account_number, amount)
        message = msg
        message_type = 'success' if success else 'error'
    
    return render_template('withdraw.html', message=message, message_type=message_type)

@app.route('/balance', methods=['GET', 'POST'])
@login_required
def balance():
    """Check balance page"""
    account = None
    message = ''
    message_type = ''
    
    if request.method == 'POST':
        account_number = request.form.get('account_number')
        success, msg, account_data = bank.check_balance(account_number)
        
        if success:
            account = account_data
            message = msg
            message_type = 'success'
        else:
            message = msg
            message_type = 'error'
    
    return render_template('balance.html', account=account, message=message, message_type=message_type)

@app.route('/all_accounts')
@login_required
def all_accounts():
    """Display all accounts page"""
    accounts = bank.get_all_accounts()
    return render_template('all_accounts.html', accounts=accounts)

@app.route('/modify', methods=['GET', 'POST'])
@login_required
def modify():
    """Modify account page"""
    account = None
    message = ''
    message_type = ''
    
    if request.method == 'POST':
        if 'search' in request.form:
            account_number = request.form.get('account_number')
            account_obj = bank.get_account(account_number)
            if account_obj:
                account = account_obj.to_dict()
            else:
                message = 'Account not found'
                message_type = 'error'
        
        elif 'update' in request.form:
            account_number = request.form.get('account_number')
            name = request.form.get('name')
            account_type = request.form.get('account_type')
            
            success, msg = bank.modify_account(account_number, name, account_type)
            message = msg
            message_type = 'success' if success else 'error'
    
    return render_template('modify.html', account=account, message=message, message_type=message_type)

@app.route('/close_account', methods=['GET', 'POST'])
@login_required
def close_account():
    """Close account page"""
    message = ''
    message_type = ''
    
    if request.method == 'POST':
        account_number = request.form.get('account_number')
        
        success, msg = bank.close_account(account_number)
        message = msg
        message_type = 'success' if success else 'error'
    
    return render_template('close_account.html', message=message, message_type=message_type)

if __name__ == '__main__':
    app.run(debug=True)