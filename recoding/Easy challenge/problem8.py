def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))

print(has_duplicates([1, 2, 3, 2]))
print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([]))