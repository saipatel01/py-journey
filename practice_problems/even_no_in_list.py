#method1
number=[1,2,3,4,5,6]
even_no=[]
for num in number:
    if num % 2==0:
        even_no.append(num)
print("Even numbers:",even_no)


#using list comprehension
numbers=[11,22,33,44,55,66]
even_number=[num for num in numbers if num%2==0]
print("even numbers:",even_number)