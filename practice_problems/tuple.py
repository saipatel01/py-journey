#wap to consider a tuple collection which consists of only 2 values check whether the tuple is homogeneos or heterogeneous

tuple=eval(input("enter a tuple of 2 values: "))
if type(tuple[0]==type(tuple[1])):
    print("hemo")
else:
    print("hetero")
