'''8. ATM Withdrawal Simulator 🏧

Problem:
Account balance and withdrawal amount input teesukoni withdrawal possible aa leda check cheyyi.

Example:

Balance = 5000
Withdraw = 2000

Output:
Transaction Successful
Remaining Balance = 3000'''

Acc_bal=int(input("enter Acc balance:"))
withdraw=int(input("enter withdraw amount:"))

remain=Acc_bal-withdraw
if Acc_bal>withdraw:
    print("Transaction succesfull")
    print("Remainig Balance =",remain)
else:
    print("insufficient balance")


