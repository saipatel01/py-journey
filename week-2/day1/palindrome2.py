#using fun
def is_palindrome(s):
    s=s.upper()
    reversed_s=s[::-1]
    return s == reversed_s
   
print(is_palindrome("Hello"))  # Should be False
print(is_palindrome("Madam"))  # Should be True


