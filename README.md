# Allowance Budget Management App

**A user-friendly expense tracking and budget management application to help you manage your finances effectively.**

The Allowance Budget App is developed to help users manage their finances effectively. It allows users to track daily expenses, monitor savings, and organize budgeting activities using a user-friendly interface.

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

✅ **Set and Manage Budgets** - Create budgets with customizable types (Monthly/Weekly)  
✅ **Track Expenses** - Add and monitor daily expenses with dates  
✅ **View Expense List** - Display all recorded expenses in an organized format  
✅ **Budget Dashboard** - Visual dashboard with budget usage percentage and progress bar  
✅ **Financial Reports** - Comprehensive reports showing budget vs expenses  
✅ **Input Validation** - Prevents negative amounts and invalid entries  
✅ **Budget Alerts** - Warnings when budget is exceeded or near the limit  

---

## Prerequisites

Before installing this application, ensure you have the following:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python Package Manager) - Usually comes with Python
- **Git** (optional, for cloning the repository) - [Download Git](https://git-scm.com/)
- A terminal or command prompt

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/SDDIO02/Allowance_Budget_Management_App.git
cd Allowance_Budget_Management_App
```

**Or manually download the repository:**
- Visit the [GitHub repository](https://github.com/SDDIO02/Allowance_Budget_Management_App)
- Click **Code** → **Download ZIP**
- Extract the ZIP file to your desired location

### Step 2: Verify Python Installation

Check if Python is installed on your system:

```bash
python --version
```

Or on some systems:

```bash
python3 --version
```

You should see Python 3.7 or higher installed.

### Step 3: Navigate to the Project Directory

```bash
cd Allowance_Budget_Management_App
```

### Step 4: Run the Application

Execute the main Python file:

```bash
python main.py
```

Or on some systems:

```bash
python3 main.py
```

The application will start and display the welcome message.

---

## Usage

Once the application is running, follow these steps:

### 1. **Enter Your Name**
   - The application will prompt you to enter your name
   - Example: `John Doe`

### 2. **Main Menu Options**

```
========== MAIN MENU ==========
1. Set Budget
2. Expense Input Screen
3. View Expenses
4. Budget Dashboard
5. Report Page
6. Exit
```

### Option 1: Set Budget
- Enter the budget amount (e.g., 5000)
- Enter budget type (e.g., Monthly or Weekly)
- Budget is set successfully!

### Option 2: Expense Input Screen
- Enter expense name (e.g., Groceries)
- Enter amount (e.g., 500)
- Enter date in MM/DD/YYYY format (e.g., 06/08/2026)
- Expense is added successfully!

### Option 3: View Expenses
- Displays all recorded expenses in a formatted list
- Shows expense name, amount, and date

### Option 4: Budget Dashboard
- Visual overview of your budget
- Shows total budget, expenses, and remaining balance
- Progress bar indicating budget usage percentage
- Alerts if budget is exceeded or near limit

### Option 5: Report Page
- Detailed financial report
- Lists all expenses with breakdown
- Shows budget status and remaining balance

### Option 6: Exit
- Closes the application

---

## Project Structure

```
Allowance_Budget_Management_App/
│
├── main.py                 # Main application file
├── README.md              # Documentation (this file)
└── .gitignore            # Git ignore file
```

---

## Code Classes

### **Expense Class**
Stores individual expense information:
- `expense_name`: Name of the expense
- `amount`: Amount spent
- `date`: Date of the expense

### **Budget Class**
Manages budget information:
- `budget_amount`: Total budget amount
- `budget_type`: Type of budget (Monthly/Weekly)

### **User Class**
Core user management:
- `name`: User's name
- `budget`: User's budget object
- `expenses`: List of expenses

### **Dashboard Class**
Displays budget overview with visual indicators

### **Report Class**
Generates comprehensive financial reports

---

## Example Usage

```
===== EXPENSE TRACKER APPLICATION =====
Enter your name: Maria Santos

========== MAIN MENU ==========
1. Set Budget
2. Expense Input Screen
3. View Expenses
4. Budget Dashboard
5. Report Page
6. Exit

Enter your choice: 1
Enter Budget Amount: ₱10000
Enter Budget Type (Monthly/Weekly): Monthly
Budget set successfully!

Enter your choice: 2
===== EXPENSE INPUT SCREEN =====
Enter Expense Name: Groceries
Enter Amount: ₱2500
Enter Date (MM/DD/YYYY): 06/01/2026
Expense added successfully!

Enter your choice: 4
===== BUDGET DASHBOARD =====
User: Maria Santos
Budget Type: Monthly
Total Budget: ₱10000.00
Total Expenses: ₱2500.00
Remaining Budget: ₱7500.00

Budget Usage:
[█████-----] 25.00%
Budget is under control.
```

---

## Troubleshooting

### Issue: "Python command not found"
**Solution:** 
- Ensure Python is installed and added to your system PATH
- Try using `python3` instead of `python`
- On Windows, reinstall Python and check "Add Python to PATH"

### Issue: "Invalid amount" error
**Solution:**
- Ensure you enter a numeric value for the amount
- Don't include currency symbols (₱ is added automatically)

### Issue: "Date format incorrect"
**Solution:**
- Always use MM/DD/YYYY format for dates
- Example: 06/08/2026 (June 8, 2026)

---

## Features Roadmap

Future enhancements:
- 💾 Data persistence (save/load data)
- 📊 Advanced charts and analytics
- 💰 Multiple currency support
- 🔔 Email notifications for budget alerts
- 📱 Mobile app version
- 🗂️ Category-based expense tracking

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## License

This project is open-source and available under the MIT License.

---

## Contact & Support

For questions or issues, please:
- Open an issue on [GitHub Issues](https://github.com/SDDIO02/Allowance_Budget_Management_App/issues)
- Contact the repository owner: SDDIO02

---

**Happy budgeting! 💰**
