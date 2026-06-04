num = int(input("Enter a number: "))

original = num

# Count digits
count = 0
temp = num

while temp > 0:
    count += 1
    temp = temp // 10

# Armstrong calculation
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total = total + (digit ** count)
    temp = temp // 10

# Compare
if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")