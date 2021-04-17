'''
This is the Budget Class App.
It receives details as name of item, amount and balance.

This class is instantiated over Food, Clothing and Entertainment.

This class has for methods which are,

Deposit: Helps you make deposit to the Budget Account. It also shows how much was deposited.

Withdrawal: Helps you make withdrawals from the Budget Account.

Balance: Displays what balance is left in the chosen category

Transfer: Help move funds from one account to another.

'''

class Budget:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balanced = balance

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balanced += amount
        print(f'You have deposited {amount} to your {self.name} account')

    def withdraw(self):
        amount = float(input("Enter amount to be withdraw: "))
        self.balanced -= amount
        print(f'You have withdrawn {amount} from your {self.name} account')

    def balance(self):
       #print("\n Net Available Balance= ",self.balanced)
       print(f'Your {self.name} account balance is {self.balanced}')

    def transfer(self, other):
        amount = float(input("Enter amount to transfer\n"))
        self.balanced -= amount 
        other.balanced += amount
        print(f'Transfer Successful.\n Your balances are now\n {other.name} Account: {other.balanced}\n {self.name} Account: {self.balanced}')


Food = Budget("Food")
Clothing = Budget("Clothing")
Entertainment = Budget("Entertainment")

#Testing Kit is added below
print("Welcome to the S O Budget App \n")
Food.deposit()
Food.withdraw()
Clothing.deposit()
Food.transfer(Clothing)
Clothing.withdraw()
Food.balance()
