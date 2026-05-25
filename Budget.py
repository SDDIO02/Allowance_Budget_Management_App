class Budget:
    def __init__(self):
        self.totalBudget = 0.0
        self.remainingBalance = 0.0

    # setBudget()
    def setBudget(self, amount):
        self.totalBudget = amount
        self.remainingBalance = amount
        print(f"Budget set to: ₱{self.totalBudget:.2f}")

    # updateBalance()
    def updateBalance(self, expense):
        if expense <= self.remainingBalance:
            self.remainingBalance -= expense
            print(f"Expense of ₱{expense:.2f} recorded.")
            print(f"Remaining Balance: ₱{self.remainingBalance:.2f}")
        else:
            print("Insufficient budget balance!")

    # Display Budget Details
    def displayBudget(self):
        print("\nBudget Details")
        print("----------------------")
        print(f"Total Budget      : ₱{self.totalBudget:.2f}")
        print(f"Remaining Balance : ₱{self.remainingBalance:.2f}")

ceate_budget = Budget()
ceate_budget.setBudget(5000.0)              
ceate_budget.updateBalance(1500.0)
ceate_budget.displayBudget()
