#wap to create a dictionary where the keys are uc,lc,sc,numbers each key has a collection,whenever user enters a string chars are divided accordingly

s="ABCxyz123%$#@"
i=0
uc,lc,sc,digit=[],[],[],[]
d={}
while i<len(s):
    char=s[i]
    if "A"<=char<="Z":
        uc.append(char)
    elif "a"<=char<="z":
        lc.append(char)
    elif "0"<=char<="9":
        digit.append(char)
    else:
        sc.append(char)
    i+=1
d["upper case"]=uc
d["lower case"]=lc
d["digit"]=digit
d["special character"]=sc
print(d)

