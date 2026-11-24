from ex1_vector import Vector
import pytest


def test_vector_change_after_init():
    data = [1, 2]
    v = Vector(data)
    data.append(3)
    data[0] = 99
    assert v == Vector([1, 2])
def test_vector_empty():
    with pytest.raises(ValueError):
        Vector([])

def test_vector_repr():
    assert repr(Vector([1, 2])) == 'Vector([1, 2])'

def test_vector_str():
    assert str(Vector([1, 2])) == '(1, 2)'

def test_vector_lenght():
    assert len(Vector([1, 2, 3])) == 3
    assert len(Vector([1, 2, 3, 4, 5])) == 5

def test_vector_comparison():
    assert Vector([1, 2]) == Vector([1, 2])
    assert Vector([1, 2]) != Vector([2, 1])
    assert Vector([1, 2]) != [1, 2]

def test_vector_sum_not_change_operands():
    v1 = Vector([1, 2])
    v2 = Vector([3, 4])
    v3 = Vector([4, 6])
    v1 + v2 == v3
    assert v1 == Vector([1, 2])
    assert v2 == Vector([3, 4])

def test_vector_sum():
    assert Vector([1, 2]) + Vector([3, 4]) == Vector([4, 6])

def test_vector_dot_product():
    assert Vector([1, 2]).dot(Vector([3, 4])) == 11

def test_vector_sum_diff_lengths():
    with pytest.raises(ValueError):
        Vector([1, 2]) + Vector([1, 2, 3])

def test_vector_add_error():
    with pytest.raises(TypeError):
        Vector([1, 2]) + 5

def test_vector_dot_error():
    with pytest.raises(TypeError):
        Vector([1, 2]).dot("hello")

def test_vector_subclass():
    class UnitVector(Vector):
        pass
    a = UnitVector([1, 2])
    b = UnitVector([1, 2])
    assert a == b
    assert repr(UnitVector([1, 2])) == 'UnitVector([1, 2])'