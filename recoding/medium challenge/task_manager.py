from collections import deque

pending_tasks = deque()
completed_tasks = []

pending_tasks.append("Study Python")
pending_tasks.append("Practise coding")
pending_tasks.append("Read documentation")

print("Pending tasks:", pending_tasks)

task = pending_tasks.popleft()
completed_tasks.append(task)
print("Completed task:", task)
print("Pending tasks:", pending_tasks)
print("Completed tasks:", completed_tasks)