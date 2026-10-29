def count_even(numbers):
    even = 0

    for num in numbers:
        if num % 2 == 0:
            even += 1
    return even


print(count_even([1, 2, 3, 4, 6]))
print(count_even( [1, 3, 5, 7]))        
