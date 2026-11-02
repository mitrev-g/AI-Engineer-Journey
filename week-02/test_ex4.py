from ex4_recursion import factorial, sum_list, flatten, fib_memo, fib_naive
import ex4_recursion
import pytest
import copy
from fractions import Fraction


@pytest.fixture(autouse=True)
def reset_call_count():
    ex4_recursion.call_count = 0


# ----- factorial -----

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_string():
    with pytest.raises(TypeError):
        factorial('s')
def test_factorial_float():
    with pytest.raises(TypeError):
        factorial(2.5)

def test_factorial_fraction():
    with pytest.raises(TypeError):
        factorial(Fraction(5, 2))

def test_factorial_bool():
    with pytest.raises(TypeError):
        factorial(True)

# ----- sum_list -----

def test_sumlist():
    assert sum_list([]) == 0
    assert sum_list([5]) == 5
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([-1, 2.5, -1.5]) == 0
    



def test_sumlist_string():
    with pytest.raises(TypeError):
        sum_list(['5'])

def test_sumlist_input_unchanged():
    nums = [3, 4, 5, 6]
    original = nums.copy()
    sum_list(nums)
    assert original == nums

# ----- flatten -----

def test_flatten():
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, [2, [3, [4]], 5]]) == [1, 2, 3, 4, 5]
    assert flatten([[], [[]], [[[[]]]]]) == []
    assert flatten([[[[[[1]]]]]]) == [1]
    assert flatten([1.5, [2]]) == [1.5, 2]


def test_flatten_input_unchanged():
    nums = [1,[2, 3]]
    original = copy.deepcopy(nums)
    flatten(nums)
    assert nums == original



# ----- fib_naive -----

def test_fib_naive():
    assert fib_naive(0) == 0
    assert fib_naive(1) == 1
    assert fib_naive(2) == 1
    assert fib_naive(10) == 55



def test_fib_naive_wrong():
    with pytest.raises(TypeError):
        fib_naive('5')

def test_fib_naive_negative():
    with pytest.raises(ValueError):
        fib_naive(-1)

def test_fib_naive_same_input():
    fib_naive(10)
    first_counter = ex4_recursion.call_count
    ex4_recursion.call_count = 0
    fib_naive(10)
    second_counter = ex4_recursion.call_count
    assert first_counter == second_counter
    

# ----- fib_memo -----

def test_fib_memo():
    assert fib_memo(0) == 0
    assert fib_memo(1) == 1
    assert fib_memo(2) == 1
    assert fib_memo(10) == 55



def test_fib_memo_wrong():
    with pytest.raises(TypeError):
        fib_memo('s')

def test_fib_memo_negative():
    with pytest.raises(ValueError):
        fib_memo(-1)

def test_fib_both():
    for i in range(0, 16):
        assert fib_naive(i) == fib_memo(i)

def test_fib_memo_same_input():
    fib_memo(10)
    first_counter = ex4_recursion.call_count
    ex4_recursion.call_count = 0
    fib_memo(10)
    second_counter = ex4_recursion.call_count
    assert first_counter == second_counter
# ----- call_count -----

def test_call_count():
    fib_naive(4)
    assert ex4_recursion.call_count == 9
    ex4_recursion.call_count = 0
    fib_memo(30)
    assert ex4_recursion.call_count == 59