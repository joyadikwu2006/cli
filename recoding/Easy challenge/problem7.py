def reverse_list(items):
    reversed_items = []
    index = len(items) - 1
    while index >= 0:
        reversed_items.append(items[index])
        index -= 1
    return reversed_items


print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))