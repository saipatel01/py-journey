#method2
n = input("Enter a number: ")

sum_digits = 0

for digit in n:
    sum_digits +=int(digit)

print("Sum of digits:", sum_digits)



#method3
n = input("Enter a number: ")
print("Sum of digits:", sum(int(digit) for digit in n))

