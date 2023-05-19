from classes import Bank, Customer, Transaction

class Main:
    def run(self):
        print("Welcome to John Cena's Bank !!!!!!")
        bank = Bank("John Cena Bank", "New York")
        print(bank)
        print("=======================================================================")

        
        customer1 = Customer("John")
        bank.add_customer(customer1)
        account1 = bank.open_account(customer1, account_id=1)
        account1.deposit(100.0)
        account1.withdraw(50.0)
        print(account1)
        transaction1 = Transaction(account1, "Transfer", 25.0)
        print(transaction1)
        print("=======================================================================")

        # User 2
        customer2 = Customer("Emily")
        bank.add_customer(customer2)
        account2 = bank.open_account(customer2, account_id=2)
        account2.deposit(200.0)
        account2.withdraw(100.0)
        print(account2)
        transaction2 = Transaction(account2, "Payment", 75.0)
        print(transaction2)
        print("=======================================================================")

        # User 3
        customer3 = Customer("Michael")
        bank.add_customer(customer3)
        account3 = bank.open_account(customer3, account_id=3)
        account3.deposit(500.0)
        account3.withdraw(200.0)
        print(account3)
        transaction3 = Transaction(account3, "Withdrawal", 150.0)
        print(transaction3)
        print("=======================================================================")

        # User 4
        customer4 = Customer("Sophia")
        bank.add_customer(customer4)
        account4 = bank.open_account(customer4, account_id=4)
        account4.deposit(1000.0)
        account4.withdraw(500.0)
        print(account4)
        transaction4 = Transaction(account4, "Deposit", 300.0)
        print(transaction4)
        print("=======================================================================")
        # User 5
        customer5 = Customer("Smith")
        bank.add_customer(customer5)
        account5 = bank.open_account(customer5, account_id=5)
        account5.deposit(11000.0)
        account5.withdraw(12000.0)
        print(account5)
        transaction5 = Transaction(account5, "Deposit", 300.0)
        print(transaction5)
        print("=======================================================================")


if __name__ == "__main__":
    main = Main()
    main.run()
