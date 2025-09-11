import sys

print("""
please select an operation:
1. Addition
2. Subtraction
3. Multiplication
""")

choice=int(input("select operation"))
if choice not in (1,2,3):
    print("invalid choice")
    sys.exit()

num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))

if choice ==1:
    result=num1+num2
elif choice ==2:
    result=num1-num2
else:
    result=num1*num2
print("the result is: ", result)

