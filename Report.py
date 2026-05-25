class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
        
class Budget:
    def __init__(self, totalBudget):
        self.totalBudget = totalBudget
        
class Report:
    def __init__(self):
        self.reportData = ""

    # generateReport()
    def generateReport(self, expenses, budget):
        totalExpenses = sum(exp.amount for exp in expenses)
        remainingBalance = budget.totalBudget - totalExpenses
        
        self.reportData = f"""
========= FINANCIAL REPORT =========
Total Budget     : ₱{budget.totalBudget:.2f}
Total Expenses   : ₱{totalExpenses:.2f}
Remaining Balance: ₱{remainingBalance:.2f}

Expense Details:
"""
        for exp in expenses:
          self.reportData += (
                f"- {exp.category}: ₱{exp.amount:.2f}\n"
            )
        return self.reportData
        
class User:
    def __init__(self, name):
        self.name = name
        self.expenses = []
        self.budget = None

    def addExpense(self, expense):
        self.expenses.append(expense)

    def setBudget(self, budget):
        self.budget = budget

# Main Program
user1 = User("Sean")
# Set Budget
budget = Budget(10000)
user1.setBudget(budget)
# Add Expenses
user1.addExpense(Expense(2500, "Food"))
user1.addExpense(Expense(1500, "Transportation"))
user1.addExpense(Expense(1000, "Bills"))
# Generate Report
report = Report()
generatedReport = report.generateReport(
    user1.expenses,
    user1.budget
)
# Display Report
print(generatedReport)
