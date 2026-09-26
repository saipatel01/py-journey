s=13.0
print(type(s))#<class 'float'>

print(int(s)) #13
print(float(s)) #13.0
print(complex(s))#(13+0j)

print(bool(s))#True
print(str(s))#13.0
#print(list(s))#TypeError: 'float' object is not iterable
#print(tuple(s))#TypeError: 'float' object is not iterable
#print(set(s))TypeError: 'float' object is not iterable
print(dict(s))