from collections import deque

queue = deque()

queue.append("joy")
queue.append("john")
queue.append("mary")

queue.popleft()

print(queue)
print("Next person:", queue[0])