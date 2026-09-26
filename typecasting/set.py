s={'sai',139,2.0,11}
print(type(s))#<class 'set'>

#print(int(s)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'

#print(float(s)) #TypeError: float() argument must be a string or a real number, not 'set'
print(complex(s))#TypeError: complex() first argument must be a string or a number, not 'tuple'

print(bool(s))#True
print(str(s))#{2.0, 11, 139, 'sai'}

print(list(s))#{2.0, 11, 139, 'sai'}

print(tuple(s))#{2.0, 11, 139, 'sai'}
print(set(s))#{2.0, 11, 139, 'sai'}
print(dict(s))#typeError: cannot convert dictionary update sequence element #0 to a sequence