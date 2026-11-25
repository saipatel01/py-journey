#  wap to find the smallest digit--->56792---->2
 
num = int(input("Enter a number: "))

smallest = num % 10

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest digit:", smallest)