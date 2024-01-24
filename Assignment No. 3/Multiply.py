def multiply_list(items):
    result = 1
    for item in items:
        result *=item
    return result 
# Example Usage
numbers = [1,2,3,4,5]
multiply_result = multiply_list(numbers)
print("Product:",multiply_result)