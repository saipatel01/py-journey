# INT VALUES

print(9**2) #81
print(6**3.0) #216.0
print(7**(2+1j)) #(17.170149772503567+30.72596852266744j)
print(5**True) #5
#print(3**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
#print(4**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'list'
#print(1**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'tuple'
#print(3**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'set'
#print(4**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'dict'


# FLOAT VALUES

print(9.0**2) #81.0
print(6.0**3.0) #216.0
print(7.0**(2+1j)) #(17.170149772503567+30.72596852266744j)
print(5.1**True) #5.1
#print(3.0**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'str'
#print(4.2**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'list'
#print(1.33**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'tuple'
#print(3.33**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'set'
#print(4.2**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'dict'


# COMPLEX VALUES

print((9+10j)**2) #(-19+180j)
print((6+0j)**3.0) #(216+0j)
print((7+2j)**(2+1j)) #(16.812935861652533+58.28175450596654j)
print((3+2j)**True) #(3+2j)
#print((4+4j)**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'complex' and 'str'
#print((4+3j)**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'complex' and 'list'
#print((1+0j)**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'complex' and 'tuple'
#print((3+9j)**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'complex' and 'set'
#print((2+3j)**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'complex' and 'dict'


# BOOL VALUES

print(True**2) #1
print(True**3.0) #1.0
print(True**(10+4j)) #(1+0j)
print(True**True) #1
#print(True**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'str'
#print(True**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'list'
#print(True**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'tuple'
#print(True**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'set'
#print(True**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'dict'

# STRING VALUES

#print("sai"**2) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#print("sai"**3.0) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
#print("sai"**(10+4j)) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'complex'
#print("sai"**True) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'bool'
#print("kumar"**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
#print("sai"**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'list'
#print("sai"**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'tuple'
#print("sai"**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'set'
#print("sai"**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'dict'


# LIST VALUES

#print([20,30]**2) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
#print([20,30]**3.0) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'float'
#print([20,30]**(10+4j)) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'complex'
#print([20,30]**True) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'bool'
#print([20,30]**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'str'
#print([10,40]**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'list'
#print([20,30]**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'tuple'
#print([20,30]**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'set'
#print([20,30]**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'dict'


# TUPLE VALUES

#print((10,20)**2) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
#print((10,20)**3.0) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'float'
#print((10,20)**(10+4j)) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'complex'
#print((10,20)**True) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'bool'
#print((10,20)**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'str'
#print((10,20)**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'list'
#print((10,20)**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'tuple'
#print((10,20)**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'set'
#print((10,20)**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'dict'


# SET VALUES

#print({5,6,7}**2) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'int'
#print({5,6,7}**3.0) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'float'
#print({5,6,7}**(10+4j)) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'complex'
#print({5,6,7}**True) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'bool'
#print({5,6,7}**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'str'
#print({5,6,7}**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'list'
#print({5,6,7}**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'tuple'
#print({5,6,7}**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'set'
#print({5,6,7}**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'dict'


# DICT VALUES

#print({'sai':'kumar','patel':'saab'}**2) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'int'
#print({'sai':'kumar','patel':'saab'}**3.0) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'float'
#print({'sai':'kumar','patel':'saab'}**(10+4j)) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'complex'
#print({'sai':'kumar','patel':'saab'}**True) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'bool'
#print({'sai':'kumar','patel':'saab'}**"sai") #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'str'
#print({'sai':'kumar','patel':'saab'}**[20,30]) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'list'
#print({'sai':'kumar','patel':'saab'}**(40,59)) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'tuple'
#print({'sai':'kumar','patel':'saab'}**{2,3,4}) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'set'
#print({'sai':'kumar','patel':'saab'}**{2:3,5:5}) #TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'dict'