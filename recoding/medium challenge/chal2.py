def move_Zeros(numbers):
    end = 0
    
    for first in range(len(numbers)):
        if numbers[first] != 0:
            numbers[end], numbers[first] = numbers[first], numbers[end]
            end += 1
    return numbers        

print(move_Zeros([0, 1, 0, 3, 12]))
print(move_Zeros([4, 0, 5, 0, 2]))
print(move_Zeros([1, 2, 3]))