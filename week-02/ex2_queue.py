from collections import deque
import time

class DequeQueue():
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            return None

        removed = self.queue.popleft()
        return removed

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

class ListQueue():
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        
        return removed
    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    def __len__(self):
        
        return len(self.queue)


    