s=['sai',139,2.0,11]
#print(type(s))#<class 'list'>

#print(int(s)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

#print(float(s)) #TypeError: float() argument must be a string or a real number, not 'list'
#print(complex(s))#TypeError: complex() first argument must be a string or a number, not 'list'

print(bool(s))#True
print(str(s))#['sai', 139, 2.0, 11]

print(list(s))#['sai', 139, 2.0, 11]

print(tuple(s))#['sai', 139, 2.0, 11]

print(set(s))
print(dict(s))