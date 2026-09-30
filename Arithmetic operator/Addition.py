#float values
print(9.0+2) #11.0
print(6.0+3.0)#9.0
print(7.0+(10+4j))#(17+4j)
print(5.1+True) #6.1
#print(3.0+"sai") #TypeError: unsupported operand type(s) for +: 'float' and 'str'
#print(4.2+[20,30]) #TypeError: unsupported operand type(s) for +: 'float' and 'list'
#print(1.33+(40,59))#TypeError: unsupported operand type(s) for +: 'float' and 'tuple'
#print(3.33+{2,3,4}) #TypeError: unsupported operand type(s) for +: 'float' and 'set'
#print(4.2+{2:3,5:5}) #TypeError: unsupported operand type(s) for +: 'float' and 'dict'


#commplex
print((9+10j)+2) #(11+10j)
print((6+0j)+3.0)#(9+0j)
print((7+2j)+(10+4j))#(17+6j)
print((3+2j)+True) #(4+2j)
#print((4+4j)+"sai") #TypeError: unsupported operand type(s) for +: 'complex' and 'str'
#print((4+3j)+[20,30]) #TypeError: unsupported operand type(s) for +: 'complex' and 'list'
#print((1+0j)+(40,59))#TypeError: unsupported operand type(s) for +: 'complex' and 'tuple'
#print((3+9j)+{2,3,4}) #TypeError: unsupported operand type(s) for +: 'complex' and 'set'
#print((2+3j)+{2:3,5:5}) #TypeError: unsupported operand type(s) for +: 'complex' and 'dict'

#bool
print(True+2) #3
print(True+3.0)#4.0
print(True+(10+4j))#(11+4j)
print(True+True) #2
#print(True+"sai") #TypeError: unsupported operand type(s) for +: 'bool' and 'str'
#print(True+[20,30]) #TypeError: unsupported operand type(s) for +: 'bool' and 'list'
#print(True+(40,59))#TypeError: unsupported operand type(s) for +: 'bool' and 'tuple'
#print(True+{2,3,4}) #TypeError: unsupported operand type(s) for +: 'bool' and 'set'
#print(True+{2:3,5:5}) #TypeError: unsupported operand type(s) for +: 'bool' and 'dict'


#string

#print("sai"+2) #TypeError: can only concatenate str (not "int") to str
#print("sai"+3.0)#TypeError: can only concatenate str (not "float") to str
#print("sai"+(10+4j))#TypeError: can only concatenate str (not "complex") to str
#print("sai"+True) #TypeError: can only concatenate str (not "bool") to str
print("kumar"+"sai") #kumarsai

#print("sai"+[20,30]) #TypeError: can only concatenate str (not "list") to str
#print("sai"+(40,59))#TypeError: can only concatenate str (not "tuple") to str
#print("sai"+{2,3,4}) #TypeError: can only concatenate str (not "set") to str
#print("sai"+{2:3,5:5}) #TypeError: can only concatenate str (not "dict") to str


#list
#print([20,30]+2) #TypeError: can only concatenate list (not "int") to list
#print([20,30]+3.0)#TypeError: can only concatenate list (not "float") to list
#print([20,30]+(10+4j))#TypeError: can only concatenate list (not "complex") to list
#print([20,30]+True) #TypeError: can only concatenate list (not "bool") to list
#print([20,30]+"sai") #TTypeError: can only concatenate list (not "str") to list
print([10,40]+[20,30]) #[10, 40, 20, 30]

#print([20,30]+(40,59))#TypeError: can only concatenate list (not "tuple") to list
#print([20,30]+{2,3,4}) #TTypeError: can only concatenate list (not "set") to list
#print([20,30]+{2:3,5:5}) #TypeError: can only concatenate list (not "dict") to list


#tuple
#print((10,20)+2) #TypeError: can only concatenate tuple (not "int") to tuple
#print((10,20)+3.0)#TypeError: can only concatenate tuple (not "float") to tuple
#print((10,20)+(10+4j))#TypeError: can only concatenate tuple (not "complex") to tuple
#print((10,20)+True) #TypeError: can only concatenate tuple (not "complex") to tuple
#print((10,20)+"sai") #TypeError: can only concatenate tuple (not "str") to tuple
#print((10,20)+[20,30]) #TypeError: can only concatenate tuple (not "list") to tuple

print((10,20)+(40,59))#(10, 20, 40, 59)
#print((10,20)+{2,3,4}) #TypeError: can only concatenate tuple (not "set") to tuple
#print((10,20)+{2:3,5:5}) #TypeError: can only concatenate tuple (not "dict") to tuple


#set
#print({5,6,7}+2) #TypeError: unsupported operand type(s) for +: 'set' and 'int'
#print({5,6,7}+3.0)#TypeError: unsupported operand type(s) for +: 'set' and 'float'
#print({5,6,7}+(10+4j))#TypeError: unsupported operand type(s) for +: 'set' and 'complex'
#print({5,6,7}+True) #TypeError: unsupported operand type(s) for +: 'set' and 'bool'
#print({5,6,7}+"sai") #TypeError: unsupported operand type(s) for +: 'set' and 'str'
#print({5,6,7}+[20,30]) #TypeError: unsupported operand type(s) for +: 'set' and 'list'
#print({5,6,7}+(40,59))#TypeError: unsupported operand type(s) for +: 'set' and 'tuple'
#print({5,6,7}+{2,3,4}) #TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({5,6,7}+{2:3,5:5}) #TypeError: unsupported operand type(s) for +: 'set' and 'dict'


#dict
#print({'sai':'kumar','patel':'saab'}+2) #TypeError: unsupported operand type(s) for +: 'dict' and 'int'
#print({'sai':'kumar','patel':'saab'}+3.0)#TypeError: unsupported operand type(s) for +: 'dict' and 'float'
#print({'sai':'kumar','patel':'saab'}+(10+4j))#TypeError: unsupported operand type(s) for +: 'dict' and 'complex'
#print({'sai':'kumar','patel':'saab'}+True) #TypeError: unsupported operand type(s) for +: 'dict' and 'bool'
#print({'sai':'kumar','patel':'saab'}+"sai") #TypeError: unsupported operand type(s) for +: 'dict' and 'str'
#print({'sai':'kumar','patel':'saab'}+[20,30]) #TypeError: unsupported operand type(s) for +: 'dict' and 'list'
#print({'sai':'kumar','patel':'saab'}+(40,59))#TypeError: unsupported operand type(s) for +: 'dict' and 'tuple'
#print({'sai':'kumar','patel':'saab'}+{2,3,4}) #TypeError: unsupported operand type(s) for +: 'dict' and 'set'
print({'sai':'kumar','patel':'saab'}+{2:3,5:5}) #TypeError: unsupported operand type(s) for +: 'set' and 'dict'


