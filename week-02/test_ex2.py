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
        

test_empty()
test_fifo_order()
test_peek_does_not_remove()
elapsed1 = benchmark(ListQueue, 10000)
elapsed2 = benchmark(DequeQueue, 10000)
assert elapsed1 > elapsed2
for n in (10_000, 50_000, 100_000):
    for Q in (ListQueue, DequeQueue):
        elapsed = benchmark(Q, n)
        print(f"{Q.__name__:<12} n={n:<8} {elapsed:.4f}s")