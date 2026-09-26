s=('sai',139,2.0,11)
print(type(s))#<class 'list'>

#print(int(s)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'

#print(float(s)) #TypeError: float() argument must be a string or a real number, not 'tuple'
print(complex(s))#TypeError: complex() first argument must be a string or a number, not 'list'

print(bool(s))#True
print(str(s))#('sai', 139, 2.0, 11)

print(list(s))#['sai', 139, 2.0, 11]

print(tuple(s))#('sai', 139, 2.0, 11)
print(set(s))#{11, 'sai', 2.0, 139}
print(dict(s))#ValueError: dictionary update sequence element #0 has length 3; 2 is required