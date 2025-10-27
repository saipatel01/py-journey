def is_sorted(input_list):
    for i in range(1, len(input_list)):
        # Compare current element with the previous one
        if input_list[i] < input_list[i - 1]:
            return False
    return True
print(is_sorted([10, 20, 30]))  
print(is_sorted([10, 20, 5, 30]))