#swap off first and last digits
n=int(input("number"))
arr=[]
while(n!=0):
    x=n%10
    n=n//10
    arr.append(x)
y=len(arr)
temp=arr[0]
arr[0]=arr[y-1]
arr[y-1]=temp
sum=0
arr.reverse()
for i in range(0,y):
    sum =sum*10
    sum=sum+arr[i]
    print(sum)
