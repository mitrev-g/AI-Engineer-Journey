
comparison_count = 0


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
    

# Time Complexity: O(n log n) - because it is being split in 2, the depth of the call stack is log n
# and merging all elements at all the levels is O(n) work
# Space Complexity: O(n) - because we make 2 lists at every level + 1 result list 
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

def quick_sort(nums, key=lambda x: x):
    raise(NotImplementedError)