#wap to find the product of all numbers---->56792--->3780



n = int(input("enter the number: "))
product = 1

while n > 0:
    rem = n % 10
    product = product * rem
    n = n // 10

print(product)

