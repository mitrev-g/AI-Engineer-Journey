from typing import Any
from collections.abc import Hashable


# LRUCache: dict (key → node) + doubly linked list ordered by recency
#   (most recent right after head, least recent right before tail).
# get:  O(1) average: one dict lookup + 6 pointer updates (move to front); no loops.
# put:  O(1) average: one dict lookup/insert + pointer updates + at most one eviction.
# Space: O(c), c = capacity: at most c dict entries and c nodes, plus 2 sentinels.
#   Bounded by capacity, not by how many puts happen; eviction keeps it there.
class Node():
    def __init__(self, key: Hashable, value: Any):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache():
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive int")
        self.capacity = capacity
        self.map: dict[Hashable, Node] = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        

    def _add_to_front(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        
        self.head.next = node

    def get(self, key: Hashable) -> Any | None:
        if key not in self.map:
            return None
        node = self.map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value
    
    def put(self, key: Hashable, value: Any) -> None:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            node.value = value
            self._add_to_front(node)
        else:
            node = Node(key, value)
            self._add_to_front(node)
            self.map[key] = node
            if len(self.map) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
                

    def __len__(self) -> int:
        return len(self.map)