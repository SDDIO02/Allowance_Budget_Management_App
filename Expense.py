class Expense:
    def __init__(self, amount, date, category):
        self.amount = float(amount)
        self.date = date
        self.category = category

    def addExpense(self):
        print("Expense added successfully!")

    def deleteExpense(self):
        print("Expense deleted successfully!")

    def displayExpense(self):
        print("--- Expense Details ---")
        print(f"Amount   : {self.amount}")
        print(f"Date     : {self.date}")
        print(f"Category : {self.category}")


create_expense = Expense(100.0, "2024-06-01", "Food")
create_expense.addExpense()     

create_expense.displayExpense() 
create_expense.deleteExpense()

