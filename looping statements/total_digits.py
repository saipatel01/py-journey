#wap to count the total digits in numbers ex;123456---->6
num=int(input("enter the number: "))
count = 0
while num > 0:
    count += 1
    num = num// 10
print("total no of digits in number are:",count)