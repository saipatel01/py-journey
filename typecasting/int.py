s=13
print(type(s))#<class 'int'>

print(int(s)) #13
print(float(s)) #13.0
print(complex(s))#(13+0j)

print(bool(s))#True
print(str(s))#13
#print(list(s))#TypeError: 'int' object is not iterable
#print(tuple(s))#TypeError: 'int' object is not iterable
#print(set(s))TypeError: 'int' object is not iterable
print(dict(s))#TypeError: 'int' object is not iterable