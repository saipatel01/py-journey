s="kairatabad ganesh idol"
print(s.index("a"))
print(s.index("a",2))
print(s.index("i",3))
print(s.index("a",9))
print(s.index("i",11,18)) #ValueError: substring not found




#rindex()
print(s.rindex("a"))
print(s.index("a"))
print(s.rindex("i"))
print(s.rindex("d",9))
print(s.rindex("v"))        #ValueError: substring not found