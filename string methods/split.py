s="twinkle twinkle little star"
print(s.split())
print(s.split("t"))
print(s.split("w"))
print(s.split("inkle"))


s="na savu nen sastha nik endhuku"
print(s.split("a",2))
print(s.split("a",-1))
print(s.split("a"))



#rsplit()

s="sai manchi baaludu"
print(s.split())
print(s.rsplit())
print(s.split("a"))
print(s.rsplit("a"))
print(s.split("a",2))
print(s.rsplit("a",2))