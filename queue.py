
# ASSESSMENT 3.2
# LINEAR DATA STRUCTURE: QUEUE
# LAST NAME: DELA CUESTA

from collections import deque

queue = deque()

print("================================")
print("       QUEUE - DELA CUESTA")
print("================================")

# INSERTION (ENQUEUE)
print("\nAdding letters to the queue...")

for letter in "DELACUESTA":
    queue.append(letter)

print("Queue after insertion:", list(queue))

# DELETION (DEQUEUE)
print("\nRemoving letters from the queue...")

while len(queue) > 0:
    removed = queue.popleft()

    print("\nDequeued letter:", removed)
    print("Remaining queue:", list(queue))

print("\nQueue is now EMPTY.")
print("================================")
