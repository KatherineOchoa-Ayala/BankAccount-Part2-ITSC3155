from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name: str, current_balance: float,
                 minimum_balance: float, account_number: str,
                 routing_number: str, interest_rate: float):

        super().__init__(
            customer_name,
            current_balance,
            minimum_balance,
            account_number,
            routing_number
        )

        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
