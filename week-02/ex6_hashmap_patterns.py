
# two_sum_brute
# Time: O(n²) worst case, n = len(nums): checks every pair (i, j) with i < j,
#   n(n−1)/2 pairs in total, when no pair exists or it's found at the end.
# Space: O(1): only the two loop indices; no data structure grows with n. 
def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


# two_sum
# Time: O(n), n = len(nums): one pass over the list; each step does an O(1)
#   average dict lookup and insert (a hash map's worst case is O(n) with heavy
#   collisions, which doesn't happen in practice for ints).
# Space: O(n): `seen` holds up to n entries in the worst case, when no pair
#   exists or it's found at the very end.
def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

