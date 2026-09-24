# BankAccount Python Class
# Rebecca Carpenter | 801427924

class BankAccount:
    title: str = "ITSC 3155 Bank"
    customer_name: str
    current_balance: float
    minimum_balance: float

    def __init__(self, customer_name: str, current_balance: float,
                 minimum_balance: float, account_number: str, routing_number: str) -> None:
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number


    def deposit(self, amount: float) -> None:
        self.current_balance += amount

    def withdraw(self, amount: float) -> bool:
        # if the remaining balance is less than the minimum balance, the user cannot withdraw
        if self.current_balance - amount < self.minimum_balance:
            print("Insufficient funds.")
            return False
        else:
            self.current_balance -= amount
            return True

    def print_customer_information(self) -> None:
        print("-------------------------------------")
        print(f"Bank Title: {self.title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}")
        print("-------------------------------------\n")

def main():

    # customer 1 instance
    print("Object created: Customer 1: ")
    c1 = BankAccount("John", 250, 100, "1001", "111000")
    c1.print_customer_information()

    print("Method call: Customer 1 has deposited 100.")
    c1.deposit(100)
    c1.print_customer_information()

    print("Method call: Customer 1 has withdrawn 150.")
    c1.withdraw(150)
    c1.print_customer_information()

    print("\n")

    # customer 2 instance
    print("Object created: Customer 2: ")
    c2 = BankAccount("Jane", 500, 100, "1002", "111000")
    c2.print_customer_information()

    print("Method call: Customer 2 has withdrawn 400.")
    c2.withdraw(400)
    c2.print_customer_information()

    print("Method call: Customer 2 has withdrawn 10")
    c2.withdraw(10)
    c2.print_customer_information()

if __name__ == "__main__":
    main()