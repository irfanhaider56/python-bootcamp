#Make a bank account performing functions deposit, withdraw and check balance

#check balance function
balance=int(input("Enter the balance: "))
def check_balance(total_balance):
    return total_balance
print(f"Your current balance is : {check_balance(balance)}")
#deposit amount function
def deposit(deposit_amount,balance):
    balance=deposit_amount+balance
    return balance

#withdraw amount
def withdraw(withdraw_amount,balance):
    if withdraw_amount>balance:
        print("Insufficient balance")
    else:
        balance=balance-withdraw_amount
    return balance

check_balance(balance)
deposit_amount=int(input("Enter the deposit amount:"))
balance=deposit(deposit_amount,balance)
print(f"Balance after deposit: {balance}")

withdraw_amount=int(input("Enter the withdrawal amount:"))
balance=withdraw(withdraw_amount,balance)
print(f"Balance after withdrawal money is : {balance}")