def move_Zeroes(numbers):
    end = 0
    
    for first in range(len(numbers)):
        if numbers[first] != 0:
            numbers[end], numbers[first] = numbers[first], numbers[end]
            end += 1
    return numbers        


print(move_Zeroes([0, 1, 0, 3, 12]))
print(move_Zeroes([1, 2, 3]))
print(move_Zeroes([0, 0, 5]))