s={'sai':139,'kumar':2,'sathvika':11}
print(type(s))#<class 'set'>

#print(int(s)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'

#print(float(s)) #TypeError: float() argument must be a string or a real number, not 'dict'
print(complex(s))#TypeError: complex() first argument must be a string or a number, not 'set'

print(bool(s))#True
print(str(s))#{'sai': 139, 'kumar': 2, 'sathvika': 11}

print(list(s))#['sai', 'kumar', 'sathvika']
print(tuple(s))#('sai', 'kumar', 'sathvika')
print(set(s))#{'sathvika', 'sai', 'kumar'}
print(dict(s))#{'sai': 139, 'kumar': 2, 'sathvika': 11}