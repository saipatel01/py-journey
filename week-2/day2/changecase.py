#with using input fun
def changecase(s):
   print(s.capitalize())
   print(s.upper())
   

s=input()
changecase(s)


#without using input fun
def changecase(s):
    print(s.capitalize())   # first letter capitalized
    print(s.upper())        # whole string uppercase

# Example 
changecase("sai")
changecase("kumar")


    