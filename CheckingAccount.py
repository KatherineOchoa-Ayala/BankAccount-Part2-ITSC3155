from BankAccount import BankAccount

class CheckingAccount(BankAccount): 
    TRANSFER_LIMIT = 6 # amount of transfers allowed per period (e.g., per month)

    def __init__(self, customer_name: str, current_balance: float,
                     minimum_balance: float, account_number: str,
                     routing_number: str) -> None:
    
            super().__init__(
                customer_name,
                current_balance,
                minimum_balance,
                account_number,
                routing_number
            )
            self.transfer_count = 0

    def transfer(self, amount: float, recipient_account: BankAccount) -> None: 
          if self.transfer_count >= CheckingAccount.TRANSFER_LIMIT: 
                print("Transfer limit reached for this period")
                return 

        # checking for insufficient funds 
          if not self.withdraw(amount): 
                return 

          recipient_account.deposit(amount)
          self.transfer_count += 1

          print(f"Transfered ${amount:.2f} to {recipient_account.customer_name}.")
          print(f"{self.transfer_count}/{CheckingAccount.TRANSFER_LIMIT} transfers left.")