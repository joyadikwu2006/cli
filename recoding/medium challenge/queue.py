from collections import deque

queue = deque()

queue.append("joy")
queue.append("john")
queue.append("mary")

print(queue)

queue.pop()

print(queue)