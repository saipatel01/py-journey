#  wap to find the smallest digit--->56792---->9
 
num = int(input("Enter a number: "))

greatest = num % 10

while num > 0:
    digit = num % 10

    if digit > greatest:
        greatest = digit

    num = num // 10

print("greatest digit:", greatest)