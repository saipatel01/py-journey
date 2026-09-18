#returning values with a Dictionary

def dict(a,b):
    return{
        'sum':a+b,
        'multiplication':a*b,
        'subtraction':a-b
    }
results=dict(10,20)
print("sum:",results['sum'])
print("multiplication:",results['multiplication'])
print("subtraction:",results['subtraction'])