from ex2_stack import Stack, FullStackError, StackError, EmptyStackError
import pytest


def test_stack_zero():
    with pytest.raises(ValueError):
        Stack(0)

def test_stack_negative_capacity():
    with pytest.raises(ValueError):
        Stack(-1)

def test_stack_capacity_full():
    s = Stack(2)
    s.push(1)
    s.push(2)
    with pytest.raises(FullStackError, match='full'):
        s.push(3)

def test_stack_empty_peek():
    s = Stack()
    with pytest.raises(EmptyStackError, match='empty'):
        s.peek()

def test_stack_empty_pop():
    s = Stack()
    with pytest.raises(EmptyStackError, match='empty'):
        s.pop()
        

def test_stack_returns_none():
    s = Stack()
    s.push(None)
    assert s.pop() is None
    with pytest.raises(EmptyStackError):
        s.pop()
    

def test_stack_size():
    s = Stack()
    s.push(1)
    assert s.size == 1

def test_stack_size_assignment():
    s = Stack()
    with pytest.raises(AttributeError):
        s.size = 5

def test_stack_capacity_read():
    s = Stack()
    with pytest.raises(AttributeError):
        s.capacity = 3

def test_stack_capacity():
    s = Stack()
    assert s.capacity is None
    assert Stack(3).capacity == 3

def test_stack_length():
    s = Stack()
    s.push(1)
    assert len(s) == 1

def test_stack_lifo():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_empty_error_is_stack_error():
    s = Stack()
    with pytest.raises(StackError):
        s.pop()

def test_full_error_is_stack_error():
    s = Stack(2)
    s.push(1)
    s.push(2)
    with pytest.raises(StackError):
        s.push(3)