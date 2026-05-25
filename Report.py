class Report:
    def __init__(self, user):
        self.user = user

    def displayReport(self):
        total_expenses = self.user.getTotalExpenses()
        remaining = self.user.budget.budget_amount - total_expenses

        print("\n===== REPORT PAGE =====")
        print(f"User: {self.user.name}")
        print(self.user.budget.getBudget())
        print(f"Total Expenses: ₱{total_expenses:.2f}")
        print(f"Remaining Budget: ₱{remaining:.2f}")

        print("\nExpense Details:")
        if not self.user.expenses:
            print("No expenses recorded.")
        else:
            for exp in self.user.expenses:
                print(f"- {exp.getExpense()}")

        if remaining < 0:
            print("\nYou exceeded your budget!")
        else:
            print("\nBudget is under control.")



