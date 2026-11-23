#wap to print the middle value of a string 
s=input("enter a string: ")
if len(s)!=0:
    middle_char=s[len(s)//2]
    print("middle char: ",middle_char)