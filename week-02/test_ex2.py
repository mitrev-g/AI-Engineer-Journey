from ex2_queue import ListQueue, DequeQueue
import time

def test_fifo_order():
    for Q in (ListQueue, DequeQueue):
        q = Q()
        q.enqueue(1); q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
    
def test_peek_does_not_remove():
    for Q in (ListQueue, DequeQueue):

        q = Q()
        q.enqueue(1)
        assert q.peek() == 1
        assert len(q) == 1

def test_empty():
    for Q in (ListQueue, DequeQueue):

        q = Q()
        assert q.peek() is None
        assert q.dequeue() is None

def benchmark(queue, n):
    q = queue()
    start = time.perf_counter()
    for i in range(n):
        q.enqueue(i)
    for _ in range(n):
        q.dequeue()
    elapsed = time.perf_counter() - start
        
    return elapsed
        

