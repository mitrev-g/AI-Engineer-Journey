'''
binary_search(sorted_list, target) returns the index, or -1 if the target isn’t there. 
Add a step counter and run it on list(range(1_000_000)). 
How many steps does it take at most? Why that number?
'''

def binary_search(sorted_list: list, target): 
    low = 0
    high = len(sorted_list) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if sorted_list[mid] == target:
            return (mid, steps)
        elif sorted_list[mid] > target:
            high = mid - 1
        else: 
            low = mid + 1
        
    return (-1, steps)

print(binary_search(list(range(1_000_000)), -5))
print(binary_search(list(range(1_000_000)), 500_000))
if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9], 1) == (0, 2)     # first
    assert binary_search([1, 3, 5, 7, 9], 9) == (4, 3)      # last
    assert binary_search([1, 3, 5, 7, 9], 5) == (2, 1)      # middle
    assert binary_search([1, 3, 5, 7, 9], 4) == (-1, 3)     # missing
    assert binary_search([], 3) == (-1, 0)                   # empty
    assert binary_search([5], 5) == (0, 1)                   # one element
    assert binary_search(list(range(1_000_000)), 0) == (0, 19)
    assert binary_search(list(range(1_000_000)), 999_999) == (999_999, 20)
    assert binary_search(list(range(1_000_000)), 500_000) == (500_000, 19)
    assert binary_search(list(range(1_000_000)), -5) == (-1, 19)