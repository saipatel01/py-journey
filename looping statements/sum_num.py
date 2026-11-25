# wap to count sum of numbers Ex:--->145--->10
n = int(input("Enter a number:"))

sum_digits = 0

while n > 0:
    digit = n % 10        
    sum_digits += digit   
    n = n // 10          

print("Sum of digits:", sum_digits)