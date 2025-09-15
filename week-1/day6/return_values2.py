"""Returning values with a list"""

def sai_list(a,b):
    sum=a+b
    mul=a*b
    sub=a-b
    return[sum,mul,sub]
results=sai_list(100,200)
print("Results:",results)