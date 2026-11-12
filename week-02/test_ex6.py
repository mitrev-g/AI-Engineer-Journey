from ex6_hashmap_patterns import two_sum_brute, two_sum, has_duplicates, has_duplicates_brute
import pytest
import random

# ---------- two_sum ----------
TWO_SUMS = [two_sum_brute, two_sum]

@pytest.mark.parametrize('fn', TWO_SUMS)
def test_two_sum(fn):
    assert fn([2, 7, 11, 15], 9) == (0, 1)
    assert fn([3, 2, 4], 6) == (1, 2)
    assert fn([3, 3], 6) == (0, 1)
    assert fn([1, 2], 10) is None
    assert fn([], 1) is None
    assert fn([1], 1) is None
    assert fn([-3, 4, 0, 3], 0) == (0, 3)

def is_valid_pair(nums: list[int], target: int, pair: tuple[int, int]) -> bool:
    i, j = pair
    return i < j and nums[i] + nums[j] == target
def test_two_sum_differential():
    random.seed(42)
    for _ in range(100):
        target = random.randint(-20, 20)
        length = random.randint(0, 20)
        arr = [random.randint(-10, 10) for _ in range(length)]
        brute = two_sum_brute(arr, target)
        fast = two_sum(arr, target)
        if brute is None:
            assert fast is None            # no pair exists, so fast must agree
        else:
            assert fast is not None        # a pair exists, so fast must find one too
            assert is_valid_pair(arr, target, brute)
            assert is_valid_pair(arr, target, fast)

# ---------- has_duplicates ----------

HAS_DUPL = [has_duplicates_brute, has_duplicates]

@pytest.mark.parametrize('fn', HAS_DUPL)
def test_has_duplicates(fn):
    assert fn([1, 2, 3, 4]) is False
    assert fn([1, 2, 3, 1]) is True
    assert fn([]) is False
    assert fn([1]) is False
    assert fn([5, 5]) is True
    assert fn([-1, 1, -1]) is True


def test_has_duplicates_differential():
    random.seed(42)
    for _ in range(100):
        length = random.randint(0, 20)
        arr = [random.randint(-10, 10) for _ in range(length)]
        assert has_duplicates_brute(arr) == has_duplicates(arr)


@pytest.mark.parametrize("fn", HAS_DUPL)
def test_has_duplicates_input_not_changed(fn):
    random.seed(42)
    for _ in range(10):
        nums = [random.randint(-10, 10) for _ in range(20)]
        original = nums.copy()
        fn(nums)
        assert nums == original

    
