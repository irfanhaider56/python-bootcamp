#Build a bank account system using functions deposit, withdraw, check balance 
def deposit(deposit_amount,x):
    deposit_amount=int(input("Enter the amount you want to deposit: "))
    x=x+deposit_amount
    return x
def withdraw(withdraw_amount,x):
     withdraw_amount=int(input("Enter the amount you want to withdraw: "))
     x=x-withdraw_amount
     return x
def balance(x):
    return x
print(f"Deposit amount is : {deposit(100,1000)}")
print(f"Withdraw amount is : {withdraw(100,1000)}")
print(f"Current balance is : {balance(100)}")