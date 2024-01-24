def remove_duplicates(items):
    return list(set(items))
# Example Usage
numbers = [1,2,2,3,4,4,5]
unique_numbers = remove_duplicates(numbers)
print("List without duplicates:",unique_numbers)