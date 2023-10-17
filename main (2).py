'''
Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 
'''
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        return self.__account_balance

# Create an instance of the BankAccount class
account = BankAccount("1234567890", "John Doe", 1000)

# Test deposit functionality
account.deposit(500)

# Test withdrawal functionality
account.withdraw(200)

# Test display balance functionality
balance = account.display_balance()
print("Account Balance:", balance)