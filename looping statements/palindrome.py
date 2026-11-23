s=input("enter the string:")
i=0
rev=""
while i<len(s):
    char=s[i]
    rev=char+rev
    i+=1
if s==rev:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")