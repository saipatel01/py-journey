# INT VALUES

print(9*2) #18
print(6*3.0) #18.0
print(7*(10+4j)) #(70+28j)
print(5*True) #5
print(3*"sai") #'saisaisai'
print(4*[20,30]) #[20,30,20,30,20,30,20,30]
print(2*(40,59)) #(40,59,40,59)
#print(3*{2,3,4}) #TypeError: unsupported operand type(s) for *: 'int' and 'set'
#print(4*{2:3,5:5}) #TypeError: unsupported operand type(s) for *: 'int' and 'dict'


# FLOAT VALUES

print(9.0*2) #18.0
print(6.0*3.0) #18.0
print(7.0*(10+4j)) #(70+28j)
print(5.1*True) #5.1
#print(3.0*"sai") #TypeError: can't multiply sequence by non-int of type 'float'
#print(4.2*[20,30]) #TypeError: can't multiply sequence by non-int of type 'float'
#print(1.33*(40,59)) #TypeError: can't multiply sequence by non-int of type 'float'
#print(3.33*{2,3,4}) #TypeError: unsupported operand type(s) for *: 'float' and 'set'
#print(4.2*{2:3,5:5}) #TypeError: unsupported operand type(s) for *: 'float' and 'dict'

# COMPLEX VALUES
print((9+10j)*2) #(18+20j)
print((6+0j)*3.0) #(18+0j)
print((7+2j)*(10+4j)) #(62+48j)
print((3+2j)*True) #(3+2j)
#print((4+4j)*"sai") #TypeError: can't multiply sequence by non-int of type 'complex'
#print((4+3j)*[20,30]) #TypeError: can't multiply sequence by non-int of type 'complex'
#print((1+0j)*(40,59)) #TypeError: can't multiply sequence by non-int of type 'complex'
#print((3+9j)*{2,3,4}) #TypeError: unsupported operand type(s) for *: 'complex' and 'set'
#print((2+3j)*{2:3,5:5}) #TypeError: unsupported operand type(s) for *: 'complex' and 'dict'


# BOOL VALUES

print(True*2) #2
print(True*3.0) #3.0
print(True*(10+4j)) #(10+4j)
print(True*True) #1
print(True*"sai") #'sai'
print(True*[20,30]) #[20,30]
print(True*(40,59)) #(40,59)
#print(True*{2,3,4}) #TypeError: unsupported operand type(s) for *: 'bool' and 'set'
#print(True*{2:3,5:5}) #TypeError: unsupported operand type(s) for *: 'bool' and 'dict'

# STRING VALUES

print("sai"*2) #'saisai'
#print("sai"*3.0) #TypeError: can't multiply sequence by non-int of type 'float'
#print("sai"*(10+4j)) #TypeError: can't multiply sequence by non-int of type 'complex'
print("sai"*True) #'sai'
#print("kumar"*"sai") #TypeError: can't multiply sequence by non-int of type 'str'
#print("sai"*[20,30]) #TypeError: can't multiply sequence by non-int of type 'list'
#print("sai"*(40,59)) #TypeError: can't multiply sequence by non-int of type 'tuple'
#print("sai"*{2,3,4}) #TypeError: can't multiply sequence by non-int of type 'set'
#print("sai"*{2:3,5:5}) #TypeError: can't multiply sequence by non-int of type 'dict'


# LIST VALUES

print([20,30]*2) #[20,30,20,30]
#print([20,30]*3.0) #TypeError: can't multiply sequence by non-int of type 'float'
#print([20,30]*(10+4j)) #TypeError: can't multiply sequence by non-int of type 'complex'
print([20,30]*True) #[20,30]
#print([20,30]*"sai") #TypeError: can't multiply sequence by non-int of type 'str'
#print([10,40]*[20,30]) #TypeError: can't multiply sequence by non-int of type 'list'
#print([20,30]*(40,59)) #TypeError: can't multiply sequence by non-int of type 'tuple'
#print([20,30]*{2,3,4}) #TypeError: can't multiply sequence by non-int of type 'set'
#print([20,30]*{2:3,5:5}) #TypeError: can't multiply sequence by non-int of type 'dict'


# TUPLE VALUES

print((10,20)*2) #(10,20,10,20)
#print((10,20)*3.0) #TypeError: can't multiply sequence by non-int of type 'float'
#print((10,20)*(10+4j)) #TypeError: can't multiply sequence by non-int of type 'complex'
print((10,20)*True) #(10,20)
#print((10,20)*"sai") #TypeError: can't multiply sequence by non-int of type 'str'
#print((10,20)*[20,30]) #TypeError: can't multiply sequence by non-int of type 'list'
#print((10,20)*(40,59)) #TypeError: can't multiply sequence by non-int of type 'tuple'
#print((10,20)*{2,3,4}) #TypeError: can't multiply sequence by non-int of type 'set'
#print((10,20)*{2:3,5:5}) #TypeError: can't multiply sequence by non-int of type 'dict'


# SET VALUES
#print({5,6,7}*2) #TypeError: unsupported operand type(s) for *: 'set' and 'int'
#print({5,6,7}*3.0) #TypeError: unsupported operand type(s) for *: 'set' and 'float'
#print({5,6,7}*(10+4j)) #TypeError: unsupported operand type(s) for *: 'set' and 'complex'
#print({5,6,7}*True) #TypeError: unsupported operand type(s) for *: 'set' and 'bool'
#print({5,6,7}*"sai") #TypeError: unsupported operand type(s) for *: 'set' and 'str'
#print({5,6,7}*[20,30]) #TypeError: unsupported operand type(s) for *: 'set' and 'list'
#print({5,6,7}*(40,59)) #TypeError: unsupported operand type(s) for *: 'set' and 'tuple'
#print({5,6,7}*{2,3,4}) #TypeError: unsupported operand type(s) for *: 'set' and 'set'
#print({5,6,7}*{2:3,5:5}) #TypeError: unsupported operand type(s) for *: 'set' and 'dict'


# DICT VALUES

#print({'sai':'kumar','patel':'saab'}*2) #TypeError: unsupported operand type(s) for *: 'dict' and 'int'
#print({'sai':'kumar','patel':'saab'}*3.0) #TypeError: unsupported operand type(s) for *: 'dict' and 'float'
#print({'sai':'kumar','patel':'saab'}*(10+4j)) #TypeError: unsupported operand type(s) for *: 'dict' and 'complex'
#print({'sai':'kumar','patel':'saab'}*True) #TypeError: unsupported operand type(s) for *: 'dict' and 'bool'
#print({'sai':'kumar','patel':'saab'}*"sai") #TypeError: unsupported operand type(s) for *: 'dict' and 'str'
#print({'sai':'kumar','patel':'saab'}*[20,30]) #TypeError: unsupported operand type(s) for *: 'dict' and 'list'
#print({'sai':'kumar','patel':'saab'}*(40,59)) #TypeError: unsupported operand type(s) for *: 'dict' and 'tuple'
#print({'sai':'kumar','patel':'saab'}*{2,3,4}) #TypeError: unsupported operand type(s) for *: 'dict' and 'set'
#print({'sai':'kumar','patel':'saab'}*{2:3,5:5}) #TypeError: unsupported operand type(s) for *: 'dict' and 'dict'