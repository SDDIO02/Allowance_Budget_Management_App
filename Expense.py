class Expense:
    def __init__(self, expense_name: str, amount: float, date: str):
        self.expense_name: str = expense_name
        self.amount: float = amount
        self.date: str = date

    def getExpense(self):
        return f"{self.expense_name} - ₱{self.amount:.2f} on {self.date}"

