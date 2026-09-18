#using function
def revString():
    s="Hello"
    print(s[::-1])    
revString()


#another way
def reverse_string(s):
    reversed_s = s[::-1]
    print("Input:", s)
    print("Output:", reversed_s)
    print("Explanation: Reverse of", s, "is", reversed_s)

reverse_string("Sai")
