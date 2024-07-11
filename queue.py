#IMPLEMENTIN QUEUE WITH LIST AND DEQUE

#with list
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
#['a', 'b', 'c']
print(queue.pop(0))
#'a'

#with deque
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print(q)
# deque(['a', 'b', 'c'])
print(q.popleft())
#'a'