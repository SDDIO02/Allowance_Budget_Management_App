class Budget:
    def __init__(self, budget_amount: float = 0.0, budget_type: str = "Not Set"):
        self.budget_amount: float = budget_amount
        self.type: str = budget_type

    def setBudget(self, amount: float, budget_type: str):
        self.budget_amount: float = amount
        self.type: str = budget_type

    def getBudget(self):
        return f"Budget Type: {self.type}, Amount: ₱{self.budget_amount:.2f}"
