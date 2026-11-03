import time
from test_ex2 import test_peek_does_not_remove, test_fifo_order, test_empty, benchmark
from ex2_queue import ListQueue, DequeQueue

test_empty()
test_fifo_order()
test_peek_does_not_remove()
elapsed1 = benchmark(ListQueue, 10000)
elapsed2 = benchmark(DequeQueue, 10000)
assert elapsed1 > elapsed2

if __name__ == "__main__":

    for n in (10_000, 50_000, 100_000):
        for Q in (ListQueue, DequeQueue):
            elapsed = benchmark(Q, n)
            print(f"{Q.__name__:<12} n={n:<8} {elapsed:.4f}s")