n=int(input("enter no"))
total=0
for i in range(1,n):
    if n % i ==0:
        total+=i
if total==n:
    print("perfect no")
else:
    print("not a perfect no")