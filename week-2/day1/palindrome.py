#method 1
s="madam"
low=0
high=len(s)-1

while low < high:
    if s[low]!=s[high]:
     print("no")
    low=low+1
    high=high-1
else:
   print("yes")

    