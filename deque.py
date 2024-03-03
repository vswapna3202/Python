# This program demonstrates the operations on dequeues where insert or removal
# of elements are allowed on both sides of the queue. Operations performed in this
# program are append, pop, popleft and appendleft on an empty queue.
# Input: The first line contains an integer N, the number of operations.
#        The next N lines contains the space separated names of methods and 
#        their values
# Output: Print the space separated elements of deque.
from collections import deque
n = int(input())
commands_list = []
for _ in range(n):
    inputs = input().split()
    commands_list.append([inputs[0], int(inputs[1]) if len(inputs) > 1 else None])
d = deque()
for  command, number in commands_list:
    if command == 'append':
        d.append(number)
    elif command == 'appendleft':
        d.appendleft(number)
    elif command == 'pop':
        d.pop()
    elif command == 'popleft':
        d.popleft()
print(*d)
