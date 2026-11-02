
call_count = 0

# Time: O(n), n = input value: one recursive call per level, n calls, O(1) work each
# Space: O(n): max call-stack depth is n frames
def factorial(n):
    if type(n) is not int:
        raise TypeError("value must be int")
    if n < 0:
        raise ValueError("value must be 0 or positive")
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Time: O(n²), n = len(nums): n calls, each slice copies up to n elements → n(n−1)/2 copies in total
# Space: O(n²): at max depth all n frames are alive at once, each holding its own slice → n(n−1)/2 elements
# def sum_list(nums):
#     if len(nums)==0:
#         return 0
#     else:
#         return nums[0] + sum_list(nums[1:])


# Time Complexity: O(n) - performs n + 1 amount of calls, doing O(1) work because accessing a list by index is O(1)
# Space Complexity: O(n) - at its peak, when there are n+1 amount of stack frames, the only thing that uses memory is
# n+1 amount of indexes, each call holds a reference to nums, not a copy
def sum_list(nums):
    return _sum_from(nums, 0)


def _sum_from(nums, i):
    if i == len(nums):
        return 0

    return _sum_from(nums, i + 1) + nums[i]


def flatten(nested):
    raise NotImplementedError

def fib_naive(n):
    raise NotImplementedError

def fib_memo(n):
    raise NotImplementedError