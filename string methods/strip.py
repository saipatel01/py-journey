s="      helloooooo   "
print(len(s))
print(s.strip())
print(len(s.strip()))


s1="$$$$$$$ arey evara miranthaa$$$$$$"
print(s1.strip("$"))

s2="#######hello ###### world######"
print(s2.strip("#"))


s3="@#$% python session %$#@"
print(s3.strip("@#$%"))


#lstrip()

print(s.lstrip())
print(len(s.strip()))
print(s1.lstrip("$"))
print(s2.strip("#"))
print(s3.strip("@#$%"))



#rstrip()

print(s.rstrip())
print(s1.rstrip("$"))
print(s2.strip("#"))
print(s3.strip("@#$%"))