#method 1
n = int(input("Enter a number:"))

sum_digits = 0

while n > 0:
    digit = n % 10        # Get last digit
    sum_digits += digit   # Add to sum
    n = n // 10           # Remove last digit

print("Sum of digits:", sum_digits)
