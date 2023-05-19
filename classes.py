class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.accounts = []
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def open_account(self, customer, account_id):
        account = Account(account_id, customer)
        self.accounts.append(account)
        return account

    def __str__(self):
        return f"Bank: {self.name}, Location: {self.location}"

class Account:
    def __init__(self, account_id, owner, balance_limit=10000.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = 0
        self.transactions = []
        self.balance_limit = balance_limit

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(self, "Deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if self.balance >= amount <= self.balance_limit:
            self.balance -= amount
            self.transactions.append(Transaction(self, "Withdrawal", amount))
        else:
            print("Insufficient balance or exceeds balance limit.")

    def __str__(self):
        return f"Account ID: {self.account_id}, Owner: {self.owner.name}, Balance: {self.balance}"



class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer: {self.name}"


class Transaction:
    def __init__(self, account, transaction_type, amount):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

    def __str__(self):
        return f"Transaction Type: {self.transaction_type}, Amount: {self.amount}"



