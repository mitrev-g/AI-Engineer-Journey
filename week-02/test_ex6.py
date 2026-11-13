from ex6_hashmap_patterns import two_sum_brute, two_sum, has_duplicates, has_duplicates_brute, first_unique_char, first_unique_char_brute, group_anagram, group_anagram_brute, max_window_sum, max_window_sum_brute, longest_unique_substring, longest_unique_substring_brute
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

    
# ---------- first_unique_char ----------
CHARS = [first_unique_char_brute, first_unique_char]

@pytest.mark.parametrize('fn', CHARS)
def test_first_unique_char(fn):
    assert fn('leetcode') == 0
    assert fn('loveleetcode') == 2
    assert fn('aabb') == -1
    assert fn('') == -1
    assert fn('z') == 0
    assert fn('aabbc') == 4

def test_first_unique_char_differential():
    random.seed(42)
    for _ in range(100):
        length = random.randint(0, 15)
        rand_str = ("".join(random.choice("abc") for _ in range(length)))
        assert first_unique_char_brute(rand_str) == first_unique_char(rand_str)


# ---------- group_anagram ----------

ANAGRAM = [group_anagram_brute, group_anagram]
def normalise(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)

@pytest.mark.parametrize('fn', ANAGRAM)
def test_group_anagram(fn):
    assert normalise(fn(["eat", "tea", "tan", "ate", "nat", "bat"])) == normalise([["eat","tea","ate"], ["tan","nat"], ["bat"]])
    assert normalise(fn([])) == normalise([])
    assert normalise(fn(["abc"])) == normalise([["abc"]])
    assert normalise(fn(["abc", "bca", "cab"])) == normalise([["abc","bca","cab"]])
    assert normalise(fn(["abc", "def", "ghi"])) == normalise([["abc"], ["def"], ["ghi"]])
    assert normalise(fn(["a", "a"])) == normalise([["a","a"]])
    assert normalise(fn(["aab", "abb"])) == normalise([["aab"], ["abb"]])
    assert normalise(fn(["ab", "abb"])) == normalise([["ab"], ["abb"]])
    assert normalise(fn(["", ""])) == normalise([["", ""]])

def test_group_anagram_differential():
    random.seed(42)
    for _ in range(100):
        words = ["".join(random.choice('abc') for _ in range(random.randint(0, 4))) for _ in range(10)]
        assert normalise(group_anagram(words)) == normalise(group_anagram_brute(words))

# ---------- max_window_sum ----------

WINDOW_SUM = [max_window_sum_brute, max_window_sum]

@pytest.mark.parametrize('fn', WINDOW_SUM)
def test_max_window_sum(fn):
    assert fn([2, 1, 5, 1, 3, 2], 3) == 9
    assert fn([2, 1, 5, 1, 3, 2], 1) == 5
    assert fn([2, 1, 5, 1, 3, 2], 6) == 14
    assert fn([-3, -1, -2], 2) == -3
    assert fn([1, 2], 3) is None 
    assert fn([], 1) is None 

@pytest.mark.parametrize('fn', WINDOW_SUM)
def test_max_window_sum_negative_k(fn):
    with pytest.raises(ValueError):
        fn([1,2,3], 0)

def test_max_window_sum_differential():
    random.seed(42)
    for _ in range(100):
        nums = [random.randint(-10, 10) for _ in range(random.randint(0, 15))]
        k = random.randint(1, len(nums) + 2)
        assert max_window_sum(nums, k) == max_window_sum_brute(nums, k)

# ---------- longest_unique_substring ----------

LONGEST = [longest_unique_substring_brute, longest_unique_substring]

@pytest.mark.parametrize('fn', LONGEST)
def test_longest_unique_substring(fn):
    assert fn("abcabcbb") == 3
    assert fn("bbbbb") == 1
    assert fn("pwwkew") == 3
    assert fn("") == 0
    assert fn("abcdef") == 6
    assert fn("abba") == 2
    assert fn("a") == 1

def test_longest_unique_substring_differential():
    random.seed(42)
    for _ in range(100):
        word = ("".join(random.choice('abcd') for _ in range(random.randint(0, 15))))
        assert longest_unique_substring(word) == longest_unique_substring_brute(word)
