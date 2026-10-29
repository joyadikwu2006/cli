def balanced_brackets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


print(balanced_brackets("(hello)"))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([)]"))
print(balanced_brackets("((hello)"))