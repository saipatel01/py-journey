# INT VALUES

print(9//2) #4
print(6//3.0) #2.0
#print(7//(10+4j)) #TypeError: unsupported operand type(s) for //: 'int' and 'complex'
print(5//True) #5
#print(3//"sai") #TypeError: unsupported operand type(s) for //: 'int' and 'str'
#print(4//[20,30]) #TypeError: unsupported operand type(s) for //: 'int' and 'list'
#print(1//(40,59)) #TypeError: unsupported operand type(s) for //: 'int' and 'tuple'
#print(3//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'int' and 'set'
#print(4//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'int' and 'dict'


# FLOAT VALUES

print(9.0//2) #4.0
print(6.0//3.0) #2.0
#print(7.0//(10+4j)) #TypeError: unsupported operand type(s) for //: 'float' and 'complex'
print(5.1//True) #5.0
#print(3.0//"sai") #TypeError: unsupported operand type(s) for //: 'float' and 'str'
#print(4.2//[20,30]) #TypeError: unsupported operand type(s) for //: 'float' and 'list'
#print(1.33//(40,59)) #TypeError: unsupported operand type(s) for //: 'float' and 'tuple'
#print(3.33//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'float' and 'set'
#print(4.2//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'float' and 'dict'


# COMPLEX VALUES

#print((9+10j)//2) #TypeError: unsupported operand type(s) for //: 'complex' and 'int'
#print((6+0j)//3.0) #TypeError: unsupported operand type(s) for //: 'complex' and 'float'
#print((7+2j)//(10+4j)) #TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
#print((3+2j)//True) #TypeError: unsupported operand type(s) for //: 'complex' and 'bool'
#print((4+4j)//"sai") #TypeError: unsupported operand type(s) for //: 'complex' and 'str'
#print((4+3j)//[20,30]) #TypeError: unsupported operand type(s) for //: 'complex' and 'list'
#print((1+0j)//(40,59)) #TypeError: unsupported operand type(s) for //: 'complex' and 'tuple'
#print((3+9j)//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'complex' and 'set'
#print((2+3j)//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'complex' and 'dict'


# BOOL VALUES

print(True//2) #0
print(True//3.0) #0.0
#print(True//(10+4j)) #TypeError: unsupported operand type(s) for //: 'bool' and 'complex'
print(True//True) #1
#print(True//"sai") #TypeError: unsupported operand type(s) for //: 'bool' and 'str'
#print(True//[20,30]) #TypeError: unsupported operand type(s) for //: 'bool' and 'list'
#print(True//(40,59)) #TypeError: unsupported operand type(s) for //: 'bool' and 'tuple'
#print(True//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'bool' and 'set'
#print(True//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'bool' and 'dict'


# STRING VALUES

#print("sai"//2) #TypeError: unsupported operand type(s) for //: 'str' and 'int'
#print("sai"//3.0) #TypeError: unsupported operand type(s) for //: 'str' and 'float'
#print("sai"//(10+4j)) #TypeError: unsupported operand type(s) for //: 'str' and 'complex'
#print("sai"//True) #TypeError: unsupported operand type(s) for //: 'str' and 'bool'
#print("kumar"//"sai") #TypeError: unsupported operand type(s) for //: 'str' and 'str'
#print("sai"//[20,30]) #TypeError: unsupported operand type(s) for //: 'str' and 'list'
#print("sai"//(40,59)) #TypeError: unsupported operand type(s) for //: 'str' and 'tuple'
#print("sai"//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'str' and 'set'
#print("sai"//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'str' and 'dict'


# LIST VALUES

#print([20,30]//2) #TypeError: unsupported operand type(s) for //: 'list' and 'int'
#print([20,30]//3.0) #TypeError: unsupported operand type(s) for //: 'list' and 'float'
#print([20,30]//(10+4j)) #TypeError: unsupported operand type(s) for //: 'list' and 'complex'
#print([20,30]//True) #TypeError: unsupported operand type(s) for //: 'list' and 'bool'
#print([20,30]//"sai") #TypeError: unsupported operand type(s) for //: 'list' and 'str'
#print([10,40]//[20,30]) #TypeError: unsupported operand type(s) for //: 'list' and 'list'
#print([20,30]//(40,59)) #TypeError: unsupported operand type(s) for //: 'list' and 'tuple'
#print([20,30]//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'list' and 'set'
#print([20,30]//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'list' and 'dict'


# TUPLE VALUES

#print((10,20)//2) #TypeError: unsupported operand type(s) for //: 'tuple' and 'int'
#print((10,20)//3.0) #TypeError: unsupported operand type(s) for //: 'tuple' and 'float'
#print((10,20)//(10+4j)) #TypeError: unsupported operand type(s) for //: 'tuple' and 'complex'
#print((10,20)//True) #TypeError: unsupported operand type(s) for //: 'tuple' and 'bool'
#print((10,20)//"sai") #TypeError: unsupported operand type(s) for //: 'tuple' and 'str'
#print((10,20)//[20,30]) #TypeError: unsupported operand type(s) for //: 'tuple' and 'list'
#print((10,20)//(40,59)) #TypeError: unsupported operand type(s) for //: 'tuple' and 'tuple'
#print((10,20)//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'tuple' and 'set'
#print((10,20)//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'tuple' and 'dict'


# SET VALUES

#print({5,6,7}//2) #TypeError: unsupported operand type(s) for //: 'set' and 'int'
#print({5,6,7}//3.0) #TypeError: unsupported operand type(s) for //: 'set' and 'float'
#print({5,6,7}//(10+4j)) #TypeError: unsupported operand type(s) for //: 'set' and 'complex'
#print({5,6,7}//True) #TypeError: unsupported operand type(s) for //: 'set' and 'bool'
#print({5,6,7}//"sai") #TypeError: unsupported operand type(s) for //: 'set' and 'str'
#print({5,6,7}//[20,30]) #TypeError: unsupported operand type(s) for //: 'set' and 'list'
#print({5,6,7}//(40,59)) #TypeError: unsupported operand type(s) for //: 'set' and 'tuple'
#print({5,6,7}//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'set' and 'set'
#print({5,6,7}//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'set' and 'dict'


# DICT VALUES

#print({'sai':'kumar','patel':'saab'}//2) #TypeError: unsupported operand type(s) for //: 'dict' and 'int'
#print({'sai':'kumar','patel':'saab'}//3.0) #TypeError: unsupported operand type(s) for //: 'dict' and 'float'
#print({'sai':'kumar','patel':'saab'}//(10+4j)) #TypeError: unsupported operand type(s) for //: 'dict' and 'complex'
#print({'sai':'kumar','patel':'saab'}//True) #TypeError: unsupported operand type(s) for //: 'dict' and 'bool'
#print({'sai':'kumar','patel':'saab'}//"sai") #TypeError: unsupported operand type(s) for //: 'dict' and 'str'
#print({'sai':'kumar','patel':'saab'}//[20,30]) #TypeError: unsupported operand type(s) for //: 'dict' and 'list'
#print({'sai':'kumar','patel':'saab'}//(40,59)) #TypeError: unsupported operand type(s) for //: 'dict' and 'tuple'
#print({'sai':'kumar','patel':'saab'}//{2,3,4}) #TypeError: unsupported operand type(s) for //: 'dict' and 'set'
#print({'sai':'kumar','patel':'saab'}//{2:3,5:5}) #TypeError: unsupported operand type(s) for //: 'dict' and 'dict'