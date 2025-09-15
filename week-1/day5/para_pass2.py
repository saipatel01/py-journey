#with IDs
v=19

def bujji(v):
    print(id(v))
    v=39
    print(id(v))


print(id(v))
bujji(v)
print(id(v))


#with list
s=[22,33,44]

def fun(s):
    print(id(s))
    s.append(66)
    print(id(s))

print(id(s))
fun(s)
print(id(s))    