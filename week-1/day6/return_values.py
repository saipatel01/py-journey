#returning multiple values with a Tuple
def calculate(a,b):
    sum_result=a+b
    mul_result=a*b
    sub_result=a-b
    return sum_result,mul_result,sub_result


s,m,sub=calculate(2,3)
print("sum:",s)
print("multiplication:",m)
print("subtraction:",sub)