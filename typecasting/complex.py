s=12+5j
print(type(s))#<class 'complex'>


#print(int(s)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

#print(float(s)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
print(complex(s))#(12+5j)

print(bool(s))#True
print(str(s))#(12+5j)


#print(list(s))#TypeError: 'complex' object is not iterable
#print(tuple(s))#TypeError: 'complex' object is not iterable
print(set(s))#TypeError: 'complex' object is not iterable
'''print(dict(s))#TypeError: 'complex' object is not iterable'''