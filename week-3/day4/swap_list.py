s=[0,1,2,3,4,5,6]
list=[int(i) for i in s]
def swap(s):
    if len(s)<2:
        return s
    temp=s[0]
    s[0]=s[-1]
    s[-1]=temp
    return s
print(swap(s))