from ex5_sorting import bubble_sort, merge_sort, quick_sort
import ex5_sorting
import pytest
import random

@pytest.fixture(autouse=True)
def reset_count():
    ex5_sorting.comparison_count = 0

SORTS = [bubble_sort, merge_sort, quick_sort]

@pytest.mark.parametrize("sort", SORTS)
def test_edge_cases(sort):
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]
    assert sort([1, -3, -5, 7, -11]) == [-11, -5, -3, 1, 7]

@pytest.mark.parametrize("sort", SORTS)
def test_input_unchanged(sort):
    nums = [6, 4, 3, 6]
    original = nums.copy()
    sort(nums)
    assert original == nums

@pytest.mark.parametrize("sort", SORTS)
def test_matches_sorted(sort):
    random.seed(42)
    for _ in range (100):
        length = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(length)]
        assert sort(nums) == sorted(nums)

def test_bubble_comparison_sorted():
    bubble_sort([1,2,3,4,5,6,7,8,9,10])
    assert ex5_sorting.comparison_count == 9
    # it is 9, because the list is sorted and each elements is in its right place.
    # Therefore we only compare each element with the next one and there is nothing to compare the 10th element
    # with, so we stop at 9 comparisons

def test_bubble_comparison_reversed():
    bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert ex5_sorting.comparison_count == 45
    # 45, because each element must be compared with each next element.
    # Therefore it appears 45 is calculated like this: 1st element needs 9 passes,
    # 2nd needs 8, 7, 6... so it is 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45

@pytest.mark.parametrize("sort", SORTS)
def test_stability(sort):
    assert sort([(80,'Ana'), (95,'Boris'), (80,'Dimo'), (95,'Elena')],key=lambda p: p[0]) == [(80, 'Ana'),(80, 'Dimo'), (95, 'Boris'), (95, 'Elena')]


def test_quick_sort_sorted_input():
    random.seed(42)
    list1 = list(range(2000))
    assert quick_sort(list1) == list(range(2000))
    assert ex5_sorting.comparison_count < (2000 * 2000) // 10


def test_merge_sort_comparisons():
    random.seed(42)
    nums = [random.randint(-1000, 1000) for _ in range(1024)]
    merge_sort(nums)
    assert ex5_sorting.comparison_count <= 1024 * 10
