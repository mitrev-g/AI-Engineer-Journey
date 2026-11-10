import random
comparison_count = 0

# bubble_sort
# Time complexity: Best Case - O(n) - a sorted list, because of the early exit
# Worst case is O(n^2) on reversed lists, when the early exit never triggers, so iti s n(n-1)/2 which is O(n^2)
# Space complexity is O(1), but this implementation is O(n) because we copy the inputed list.
def bubble_sort(nums, key=lambda x: x):
    global comparison_count
    sorted_list = nums.copy()
    length = len(sorted_list)
    for i in range(length-1):
        swapped = False
        for j in range(length - i - 1):
            comparison_count += 1
            if key(sorted_list[j]) > key(sorted_list[j+1]):
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True
        if not swapped:
            break
    return sorted_list
    

# merge_sort
# Time: O(n log n) in best AND worst case, n = len(nums). It always splits in half
#   (log n levels) and always merges all n elements per level (slicing also copies
#   n per level, so it doesn't change the Big O).
# Space: O(n). Slices along the current path add up to n/2 + n/4 + … < n, the merge
#   result is up to n, and the stack is log n deep.
def merge_sort(nums, key=lambda x: x):
    if len(nums) == 0 or len(nums) == 1:
        return nums.copy()
    mid = len(nums) // 2
    left = merge_sort(nums[:mid], key)
    right = merge_sort(nums[mid:], key)
    return _merge(left, right, key)

def _merge(left, right, key):
    global comparison_count
    result = []
    i = 0
    j = 0
    while len(left) >  i and len(right) > j:
        comparison_count += 1
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# quick_sort
# Time, average: O(n log n), n = len(nums). A random pivot splits the list roughly
#   in half on average, so there are about log n levels, and each level compares
#   all n elements once (up to 2 comparisons each).
# Time, worst: O(n²). If the pivot is always the smallest or largest element, each
#   piece shrinks by only 1: n levels × up to n comparisons ≈ n²/2. Also n deep,
#   so large inputs could hit the recursion limit. Very unlikely with random pivots.
# Space: O(n). New lists along the current path add up to n + n/2 + n/4 + … < 2n;
#   the stack is O(log n) deep on average, O(n) in the worst case.
def quick_sort(nums, key=lambda x: x):
    global comparison_count
    if len(nums) == 0 or len(nums) == 1:
       return nums.copy()
    pivot = random.choice(nums)
    pivot_key = key(pivot)
    smaller = []
    equal = []
    bigger = []
    for el in nums:
        comparison_count += 1
        if key(el) < pivot_key:
            smaller.append(el)
        else:
            comparison_count +=1
            if key(el) > pivot_key:
                bigger.append(el)
            else:
                equal.append(el)
    smaller = quick_sort(smaller, key)
    bigger = quick_sort(bigger, key)
    return smaller + equal + bigger