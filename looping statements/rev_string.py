s=input("enter the string:")
i=0
rev=""
while i<len(s):
    char=s[i]
    rev=char+rev
    i+=1
print(rev) #nohtyp

#method 2
s=input("enter the string:")
i=0
rev=""
length=len(s)-1
while length>=i:
    char=s[length]
    rev=rev+char
    length-=1
print(rev)