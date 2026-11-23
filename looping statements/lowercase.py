#wap to convert all the lowercase char present in the string to uppercase

s="PyThoN"
i=0
result=""
while i<len(s):
    char=s[i]
    if 97<=ord(char)<=122:
        a=ord(char)-32
        result+=chr(a)
    else:
        result+=char
    i+=1
print(result)