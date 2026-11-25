#wap to check whether a number is perfect number or not

"""
Example:

Input: 6

Factors: 1, 2, 3

Sum = 1 + 2 + 3 = 6
"""
n=int(input("enter no: "))
total=0
for i in range(1,n):
    if n % i ==0:
        total+=i
if total==n:
    print("perfect no")
else:
    print("not a perfect no")