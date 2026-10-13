'''
stats(numbers) returns the mean, median, min and max without using the statistics module. 
Then read the numbers from a .txt file you create, one per line. 
Handle the cases of an empty file and a line that isn’t a number.π
'''

import math

def read_numbers(path: str) -> list[float]:
    '''Makes a list with any string that 
    can be converted to a float'''
    res = []
    with open (path) as f:
        for line in f:
            try:
                res.append(float(line))
            except ValueError:
                
                if ',' in line:
                        
                    try:
                        res.append(float(line.replace(',', '.')))
                    except ValueError:
                        print(f"{line} can not be added to the list")
                
    return res


def stats(numbers: list[float]) -> dict:
    '''Returns None on empty list'''
    numbers = clean_nan(numbers)
    if len(numbers) == 0:
        return None
    smallest = None
    largest = None
    median = get_median(numbers)
    mean = get_mean(numbers)
    for num in numbers:
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
    return {
        'min': smallest,
        'max': largest,
        'median': median,
        'mean': mean
    }
    
        

def get_mean(numbers: list[float]) -> float:
    '''Returns None on empty list'''
    if len(numbers) == 0:
        return None
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def get_median(numbers: list[float]) -> float:
    '''Returns None on empty list'''
    if len(numbers) == 0:
        return None
    if len(numbers) % 2 != 0:
        index = int((len(numbers) + 1) / 2) - 1
        return sorted(numbers)[index]
    else:
        idx1 = int(len(numbers) / 2) - 1
        idx2 = idx1 + 1
        arr = sorted(numbers)
        return (arr[idx1] + arr[idx2])/2

def clean_nan(numbers: list[float]) -> list[float]:
    arr = []
    for num in numbers:
        if not math.isnan(num):
            arr.append(num)
    return arr

if __name__ == "__main__":
    arr = read_numbers('numbers.txt')
    print(stats(arr))
    assert get_median([5]) == 5
    assert get_median([1, 2, 3]) == 2
    assert get_median([3, 1, 2]) == 2
    assert get_median([1, 2, 3, 4]) == 2.5
    assert get_median([4, 1, 3, 2]) == 2.5
    assert get_mean([1, 2, 3]) == 2
    assert stats([]) is None
    assert stats([3, 1, 2]) == {"min": 1, "max": 3, "median": 2, "mean": 2}
    nums = [1.0, float("nan"), float("nan"), 2.0]
    cleaned = clean_nan(nums)
    assert not any(math.isnan(x) for x in cleaned)
    assert len(nums) == 4   # original list untouched
    assert stats([float('nan')]) is None