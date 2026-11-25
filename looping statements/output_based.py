#wap to get the following output
#s="tomorrow there is no mock"
'''
{'tomorrow':3,'there':2,'no':1,'mock';1}
'''
s = "tomorrow there is no mock"

words = s.split()

d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)