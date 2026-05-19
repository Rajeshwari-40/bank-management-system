# 🏦 Bank Management System

A comprehensive web-based banking application built with Python Flask for managing bank accounts and transactions.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [System Requirements](#system-requirements)
- [Screenshots](#screenshots)
- [Project Flow](#project-flow)
- [Database Schema](#database-schema)
- [Author](#author)

---

## 🎯 Overview

The Bank Management System is a web application designed to provide basic banking operations through an intuitive user interface. It allows multiple users to register, login, and manage bank accounts with features like account creation, deposits, withdrawals, balance inquiries, and account modifications.

---

## ✨ Features

### User Management
- **User Registration**: Create new user accounts with username and password
- **User Login**: Secure authentication system
- **User Logout**: Safe session termination

### Banking Operations
1. **Create Account**: Open new bank accounts (Savings/Current)
2. **Deposit Money**: Add funds to existing accounts
3. **Withdraw Money**: Withdraw funds from accounts
4. **Check Balance**: View account balance and details
5. **View All Accounts**: Display all registered bank accounts in a table
6. **Modify Account**: Update account holder name and account type
7. **Close Account**: Permanently delete bank accounts

### Security Features
- Password-based authentication
- Session management
- Login-required access control
- Data persistence using file storage

---

## 🛠️ Technologies Used

### Backend
- **Python 3.x**: Core programming language
- **Flask**: Web framework for Python
- **Session Management**: Flask sessions for user authentication

### Frontend
- **HTML5**: Structure and content
- **CSS3**: Styling and responsive design
- **Jinja2**: Template engine for dynamic content

### Data Storage
- **File-based Storage**: 
  - `users.dat`: Stores user credentials
  - `accounts.dat`: Stores bank account information

### Development Tools
- **VS Code**: Code editor
- **Command Prompt/Terminal**: Running the application
- **Web Browser**: Chrome/Firefox/Edge for testing

---

## 📁 Project Structure

```
BankWebsite/
│
├── app.py                      # Main Flask application (routing & logic)
├── bank_account.py             # Account class definition
├── bank_operations.py          # Banking operations logic
│
├── templates/                  # HTML templates folder
│   ├── login.html             # User login page
│   ├── register.html          # User registration page
│   ├── index.html             # Dashboard/home page
│   ├── create_account.html    # Create bank account form
│   ├── deposit.html           # Deposit money form
│   ├── withdraw.html          # Withdraw money form
│   ├── balance.html           # Check balance page
│   ├── modify.html            # Modify account form
│   ├── all_accounts.html      # View all accounts table
│   └── close_account.html     # Close account form
│
├── users.dat                   # User credentials storage (auto-created)
├── accounts.dat                # Bank accounts data storage (auto-created)
└── README.md                   # Project documentation (this file)
```

---

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher installed on your system
- pip (Python package installer)

### Step 1: Clone/Download Project
```bash
# Navigate to your desired directory
cd Desktop

# If using Git
git clone <repository-url>

# Or download and extract the ZIP file
```

### Step 2: Install Dependencies
```bash
# Open terminal/command prompt in project directory
cd BankWebsite

# Install Flask
pip install flask
```

---

## ▶️ How to Run

### Method 1: Using Command Prompt (Windows)
```bash
# Navigate to project folder
cd Desktop\BankWebsite

# Run the application
python app.py
```

### Method 2: Using VS Code
1. Open VS Code
2. Open project folder: `File → Open Folder → Select BankWebsite`
3. Open Terminal: `Ctrl + ` (backtick)
4. Run command: `python app.py`

### Method 3: Using Terminal (Mac/Linux)
```bash
# Navigate to project folder
cd Desktop/BankWebsite

# Run the application
python3 app.py
```

### Access the Application
Once running, open your web browser and go to:
```
http://localhost:5000
```
or
```
http://127.0.0.1:5000
```

---

## 📖 Usage Guide

### First Time Setup

#### 1. Register a New User
- Open `http://localhost:5000`
- Click "Create New Account"
- Enter username (minimum 3 characters)
- Enter password (minimum 6 characters)
- Confirm password
- Click "Create Account"

#### 2. Login
- Enter your registered username
- Enter your password
- Click "Login"

### Banking Operations

#### Create Bank Account
1. From Dashboard, click "Create Account"
2. Enter Account Number (unique identifier)
3. Enter Account Holder Name
4. Select Account Type (Savings/Current)
5. Enter Initial Deposit amount
6. Click "Create Account"

#### Deposit Money
1. Click "Deposit Money"
2. Enter Account Number
3. Enter Deposit Amount
4. Click "Deposit Money"

#### Withdraw Money
1. Click "Withdraw Money"
2. Enter Account Number
3. Enter Withdrawal Amount
4. Click "Withdraw Money"

#### Check Balance
1. Click "Check Balance"
2. Enter Account Number
3. Click "Check Balance"
4. View complete account details

#### View All Accounts
1. Click "All Accounts"
2. View table with all registered accounts

#### Modify Account
1. Click "Modify Account"
2. Search by Account Number
3. Update Name and/or Account Type
4. Click "Update Account"

#### Close Account
1. Click "Close Account"
2. Enter Account Number
3. Confirm deletion
4. Account permanently deleted

---

## 💻 System Requirements

### Minimum Requirements
- **OS**: Windows 7/8/10/11, macOS, or Linux
- **Python**: Version 3.7 or higher
- **RAM**: 2GB minimum
- **Storage**: 50MB free space
- **Browser**: Chrome, Firefox, Edge, or Safari (latest version)

### Recommended Requirements
- **OS**: Windows 10/11 or macOS latest
- **Python**: Version 3.9 or higher
- **RAM**: 4GB or more
- **Storage**: 100MB free space
- **Browser**: Chrome or Firefox (latest version)

---

## 📸 Screenshots

### Login Page
- Professional login interface
- User registration link
- Clean, corporate design

### Dashboard
- 7 main operation cards
- User welcome message
- Logout option
- Responsive grid layout

### Banking Forms
- Create Account: Multi-field form
- Deposit/Withdraw: Simple 2-field forms
- Balance Display: Detailed account information
- All Accounts: Professional table view

---

## 🔄 Project Flow

### User Authentication Flow
```
Start
  ↓
Landing Page (Login)
  ↓
├─→ New User? → Register → Login
└─→ Existing User → Login → Dashboard
                              ↓
                        [Banking Operations]
                              ↓
                           Logout → Login Page
```

### Banking Operation Flow
```
Dashboard
  ↓
Select Operation
  ↓
├─→ Create Account → Enter Details → Submit → Success/Error Message
├─→ Deposit Money → Enter Account & Amount → Submit → Balance Updated
├─→ Withdraw Money → Enter Account & Amount → Submit → Balance Updated
├─→ Check Balance → Enter Account → Display Details
├─→ View All Accounts → Display Table
├─→ Modify Account → Search → Update Fields → Submit → Success Message
└─→ Close Account → Enter Account → Confirm → Account Deleted
  ↓
Return to Dashboard
```

### Data Flow Architecture
```
User Input (HTML Form)
        ↓
Flask Routes (app.py)
        ↓
Business Logic (bank_operations.py)
        ↓
Data Layer (bank_account.py)
        ↓
File Storage (users.dat / accounts.dat)
        ↓
Response (Success/Error Message)
        ↓
User Interface (HTML Template)
```

---

## 🗄️ Database Schema

### users.dat Format
```
username1,password1
username2,password2
username3,password3
```
**Fields:**
- Username (String)
- Password (String)

### accounts.dat Format
```
account_number,name,account_type,balance
1001,John Doe,Savings,5000.00
1002,Jane Smith,Current,10000.00
```
**Fields:**
- Account Number (String/Integer)
- Account Holder Name (String)
- Account Type (Savings/Current)
- Balance (Float)

---

## 🏗️ Code Structure

### app.py - Main Application
- Flask app initialization
- Route definitions
- User authentication logic
- Session management
- Request handling

### bank_account.py - Account Class
```python
class Account:
    - __init__()          # Initialize account
    - deposit()           # Add money
    - withdraw()          # Remove money
    - get_balance()       # Return balance
    - modify()            # Update details
    - to_dict()           # Convert to dictionary
    - __str__()           # String representation
    - from_string()       # Create from string
```

### bank_operations.py - Business Logic
```python
class BankOperations:
    - __init__()          # Initialize operations
    - load_accounts()     # Load from file
    - save_accounts()     # Save to file
    - create_account()    # Create new account
    - deposit_money()     # Deposit operation
    - withdraw_money()    # Withdraw operation
    - check_balance()     # Balance inquiry
    - get_account()       # Retrieve account
    - modify_account()    # Update account
    - close_account()     # Delete account
    - get_all_accounts()  # List all accounts
```

---

## 🎨 Design Features

### Color Scheme
- **Primary Color**: #003366 (Corporate Blue)
- **Secondary Color**: #0066cc (Light Blue)
- **Success**: #28a745 (Green)
- **Error**: #dc3545 (Red)
- **Background**: #f5f5f5 (Light Gray)
- **Text**: #333333 (Dark Gray)

### UI Features
- Responsive design
- Clean, professional layout
- Consistent navigation
- User-friendly forms
- Clear error/success messages
- Professional table displays

---

## 🔒 Security Considerations

### Implemented
- Session-based authentication
- Login required for all banking operations
- Password confirmation during registration
- Account deletion confirmation

### Future Enhancements
- Password encryption (hashing)
- Database integration (SQLite/MySQL)
- HTTPS support
- Two-factor authentication
- Transaction history logging
- Admin dashboard

---

## 🐛 Known Limitations

1. **Plain Text Storage**: Passwords stored without encryption
2. **File-based Database**: Not suitable for production use
3. **No Transaction History**: Only current balance stored
4. **Single Session**: No multi-user concurrent access handling
5. **No Email Verification**: Direct registration without verification

---

## 🚧 Future Enhancements

- [ ] Password encryption (bcrypt/SHA256)
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Transaction history feature
- [ ] PDF statement generation
- [ ] Email notifications
- [ ] Admin panel
- [ ] Multi-currency support
- [ ] Account statements
- [ ] Fund transfer between accounts
- [ ] Mobile responsive optimization

---

## 📝 How to Stop the Application

### In Command Prompt/Terminal
```
Press: Ctrl + C
Type: Y (if asked)
Press: Enter
```

### In VS Code Terminal
```
Press: Ctrl + C
```

---

## 🆘 Troubleshooting

### Issue: "Flask not installed"
**Solution:**
```bash
pip install flask
```

### Issue: "Template not found"
**Solution:**
- Ensure `templates/` folder exists
- Verify all HTML files are inside `templates/`

### Issue: "Port 5000 already in use"
**Solution:**
```bash
# Stop other Flask instances
# Press Ctrl + C in all terminals
# Run again: python app.py
```

### Issue: "Cannot connect to localhost"
**Solution:**
- Ensure `python app.py` is running
- Check terminal shows "Running on http://127.0.0.1:5000"
- Try: http://127.0.0.1:5000 instead

---

## 📚 Learning Outcomes

This project demonstrates:
- ✅ Python Flask web development
- ✅ HTML/CSS frontend design
- ✅ Session management
- ✅ File I/O operations
- ✅ Object-oriented programming
- ✅ CRUD operations
- ✅ User authentication
- ✅ Form handling
- ✅ Routing and navigation
- ✅ Template rendering

---

## 👨‍💻 Author

**Your Name**
- Project: Bank Management System
- Technology: Python Flask
- Year: 2025

---

## 📄 License

This project is created for educational purposes.

---

## 🙏 Acknowledgments

- Python Flask Documentation
- HTML/CSS Resources
- Banking System Design Patterns

---

## 📞 Contact

For any queries or issues:
- Email: your.email@example.com
- GitHub: github.com/yourusername

---

## ⭐ Project Status

**Status**: ✅ Complete and Working

**Last Updated**: May 2025

**Version**: 1.0.0

---

## 🎓 Academic Information

**Course**: [Your Course Name]  
**Semester**: [Your Semester]  
**Institution**: [Your College/University]  
**Submission Date**: [Date]

---
