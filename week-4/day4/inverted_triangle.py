n=int(input("enter no:"))
for i in range(n+1):
    for j in range(n+1-i):
        print("*",end='')
    print()