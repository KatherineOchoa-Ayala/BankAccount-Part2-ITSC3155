from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount 

def main():

    # checking account instance 1
    c1 = CheckingAccount("Bob", 500, 100, "12345", "67890")
    c1.print_customer_information()

    print("Method call: Customer has deposited $150.00")
    c1.deposit(150)
    c1.print_customer_information()

    #checking account instance 2
    c2 = CheckingAccount("Emma", 750, 100, "24689", "11100")
    c2.print_customer_information()

    print("Method call: Customer has withdrawn $200.00")
    c2.withdraw(200)
    c2.print_customer_information()

    # savings account instance 1
    s1 = SavingsAccount("Dan", 1000, 100, "01101", "10010", 0.23)
    s1.print_customer_information()

    print("Method call: Customer has widthdrawn $600.00")
    s1.withdraw(600)
    s1.print_customer_information()

    #savings account instance 2
    s2 = SavingsAccount("Sarah", 1500, 100, "01102", "11000", 0.05)
    s2.print_customer_information()

    print("Method call: Add 5% interest to Savings Account.")
    s2.add_interest()
    s2.print_customer_information()

    # test checking account transfer limit 
    print("Method call: Transfer $100 from Checking Account to Savings Account.")
    c1.transfer(100, s1)
    c1.print_customer_information()
    s1.print_customer_information()

    # test transfer limit 
    print("Test transfer limit: transfer count set to max.")
    c1.transfer_count = 6 
    c1.transfer(100, s1)
    c1.print_customer_information()


    


if __name__ == "__main__": 
    main()