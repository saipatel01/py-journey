#using fun
def printalphabets(c1,c2):
    for i in range(ord(c1),ord(c2)+1):
     print(chr(i),end=' ')
printalphabets('a','s')



#without using fun
c1="a"
c2="s"

for i  in range(ord(c1),ord(c2)+1):
   print(chr(i),end=' ')