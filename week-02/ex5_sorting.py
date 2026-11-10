
comparison_count = 0

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
    

def merge_sort(nums, key=lambda x: x):
    raise(NotImplementedError)

def quick_sort(nums, key=lambda x: x):
    raise(NotImplementedError)