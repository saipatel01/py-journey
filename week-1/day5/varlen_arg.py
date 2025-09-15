def sum_num(*elements):
    result=0
    for element in elements:
        result +=element

    return result
print(sum_num(1,2))
print(sum_num(1,2,3))
print(sum_num(1))
print(sum_num())

    