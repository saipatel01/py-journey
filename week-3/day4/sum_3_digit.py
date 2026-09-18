n=int(input("enter no"))
temp=[]
sum=0
while(n!=0):
    x=n%10
    n=n//10
    sum=sum+x
    temp.append(x)
y=len(temp)
for i in range(0,y):
    for j in range (0,y):
        if(i!=j):
            if(temp[i]==temp[j]):
                sum=0
    print(sum)
