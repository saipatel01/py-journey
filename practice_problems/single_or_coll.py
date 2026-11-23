#wap to check whether the given value is single value or collection
data = eval(input("enter the data:"))
if type(data) in (list,tuple,set,dict):
    print(f"{data} is a collection ")
else:
    print(f"{data} is a single value")