n = input("Enter a number: ")
digits = len(n)

total = 0

for digit in n:
    total += int(digit) ** digits

if total == int(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
