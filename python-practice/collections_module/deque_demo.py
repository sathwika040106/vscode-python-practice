from collections import deque

numbers = deque([1, 2, 3])

numbers.appendleft(0)
numbers.append(4)

print(numbers)

numbers.pop()
print(numbers)