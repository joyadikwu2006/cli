def second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        if largest is None:
            largest = num
        elif num > largest:
            second = largest
            largest = num
        elif num < largest:
            if second is None or num > second:
                second = num

    return second

print(second_largest([10, 5, 8, 10, 3]))
print(second_largest([4, 4, 4]))
print(second_largest([-5, -2, -8, -3]))