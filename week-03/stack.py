class Stack():
    def __init__(self, capacity: int | None=None) -> None:
        if capacity is not None and capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self._capacity = capacity
        self._items = []

    # Time Complexity: Amortized O(1) - Just append 1 element at the end of the list, no matter the size, this action takes the same time. Worst case is O(n) (n = number of items in the stack) if by adding this 1 element, we exceed the capacity reserved for the list in memory and we need time to move the whole list in some other space in memory to have a higher capacity to be able to store the list with it's new length.
    # Space Complexity: O(1)
    def push(self, item: object) -> None:
        if len(self._items) == self._capacity:
            raise FullStackError("The stack is full") 
        self._items.append(item)

     
    # Time Complexity: O(1) - Just remove 1 element at the end of the list, no matter the size (n = number of items in the stack), this action takes the same time
    # Space Complexity - O(1) - We just store the popped element. Because we pop only from the end of the list, we don't have to worry about worse complexity.
    def pop(self) -> object | None:
        if len(self._items) == 0:
            raise EmptyStackError("The stack is already empty.")
        popped = self._items.pop()
        return popped

    # Time Complexity - O(1) - No matter the size  of the list (n = number of items in the stack), the action needs the same time always.
    # Space Complexity - O(1) - We don't store anything, we just check the last item on the list.
    def peek(self) -> object | None:
        if len(self._items) == 0:
            raise EmptyStackError("The stack is already empty.")
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    @property
    def size(self) -> int:
        return len(self)

    @property
    def capacity(self) -> int | None:
        return self._capacity


class StackError(Exception):
    '''
    An error with the stack has occured.
    '''
class FullStackError(StackError):
    '''
    The Stack is at full capacity.
    '''

class EmptyStackError(StackError):
    '''
    The Stack is empty.
    '''

print("hello")