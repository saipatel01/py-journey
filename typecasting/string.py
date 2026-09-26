s="sai"

print(type(s))#<class 'str'>

#print(int(s)) #ValueError: invalid literal for int() with base 10: 'sai'
#print(float(s)) #ValueError: could not convert string to float: 'sai'
#print(complex(s))#ValueError: complex() arg is a malformed string

print(bool(s))#True
print(str(s))#sai


print(list(s))#['s', 'a', 'i']
print(tuple(s))#('s', 'a', 'i')
print(set(s))
print(dict(s))