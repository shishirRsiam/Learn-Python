class Account:
    def __init__(self, name, account_no):
        self.bal = 0
        self.name = name
        self.account_no = account_no
    def balance_check(self):
        print("Hi,", self.name, "your Bank Account Balance is:", str(self.bal))
    def deposit_money(self):
        amount = int(input("Enter Deposit Ammount: "))
        self.bal += amount
        print(str(amount) + " Tk Deposit SuccessFul.")
    def withdraw_money(self):
        amount = int(input("Enter Withdraw Ammount: "))
        if amount > self.bal:
            print("Insufficient Balance")
            return
        self.bal -= amount
        print(str(amount) + " Tk Withdrawal SuccessFul!")

def showOption():
    print("Op1: Check Balance")
    print("Op2: Deposit Balance")
    print("Op3: Withdraw Balance")
    print("Op4: Back to Home")

def poccessing(op):
    if op == '1':
        customer1.balance_check()
    elif op == '2':
        customer1.deposit_money()
    elif op == '3':
        customer1.withdraw_money()
    else:
        return False


customer1 = Account("Sishir Siam", 1317129349)
print(customer1.account_no)
while True:
    showOption()
    op = input("Enter Your Option: ")
    if not poccessing(op):
        break
    print("\n")