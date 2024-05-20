class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
# 1. Instantiate the class
act1 = Account('Jose',100)
# 2. Print the object
print(act1)
# 3. Show the account owner attribute
act1.owner
# 4. Show the account balance attribute
act1.balance
# 5. Make a series of deposits and withdrawals
act1.deposit(50)

act1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
act1.withdraw(500)