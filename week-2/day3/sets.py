#creating a set
s1={10,20,30}
print(s1)

s2=set([20,30,40])
print(s2)



#adding elements
s={1,2,3}
s.add(5)
print(s)

s.update([40,60])
print(s)
#removing elements
s={20,10,30}
s.discard(30)
print(s)

s.remove(20)
print(s)

s.clear()
print(s)


