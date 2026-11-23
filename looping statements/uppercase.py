#wap to extract all the uppercase character present inside a string only if its index position is multiple of 3.

s="HELLO WORLD"
i=0
while i<len(s):
    char=s[i]
    if 65<=ord(char)<=90:
        if i%3==0:
            print(char)
    i+=1