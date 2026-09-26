s=True
print(type(s))#<class 'bool'>

print(int(s)) #1
print(float(s)) #1.0
print(complex(s))#(1+0j)

print(bool(s))#True
print(str(s))#True

#print(list(s))#TypeError: 'bool' object is not iterable
#print(tuple(s))#TypeError: 'bool' object is not iterable
#print(set(s))#TypeError: 'bool' object is not iterable
print(dict(s))#TypeError: 'bool' object is not iterable