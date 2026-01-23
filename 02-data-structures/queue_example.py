# Queue example (FIFO)

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print("Queue:", queue)

first_item = queue.popleft()
print("Removed:", first_item)
print("Queue now:", queue)
