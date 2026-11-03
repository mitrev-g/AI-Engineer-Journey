
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

# We need 2 variables to track the time and space complexity
# n = total elements at every level, numbers and inner lists included
# d = maximum depth of nested lists
# Time Complexity - O(n x d) or O(n^2) if d grows with n, each next element adds another layer in depth,
# because each number is copied once per nesting level on its way up.
# Space Complexity - O(n + d) = O(n) - number of res lists that live at the same time is equal to the amount of
# active stack frames(d) + n - the total times of calculating res - for each element at every level of every nested or non-nested list 
def flatten(nested):
  '''
  Return a new flat list of every value inside nested, at any depth, left to right.
  Anything that isn't a list (including strings) is treated as a single value; strings are out of scope.
  '''
  res = []
  for el in nested:
    if type(el) is not list:
      res.append(el)
    else:
      res.extend(flatten(el))
      
  return res


# Time complexity is O(2^n) or O(1.618ⁿ), because (depending on n) each call has to make 2 additional calls, making the amount of calls grow exponentially, and the (n-2) branch is always shorter than the (n-1), that's where 1.618ⁿ is coming from
# Space complexity is O(n), because there are only n amount of stack frames at the same time, each frame holds O(1) memory, and the maximum depth is n.
def fib_naive(n):
    if type(n) is not int:
       raise TypeError("n must be an int")
    if n < 0:
       raise ValueError("n must be a non-negative int")
    return _fib_naive(n)
    
    

def _fib_naive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return _fib_naive(n-1) + _fib_naive(n-2)

# Time: O(n): 2n - 1 calls in total, each doing O(1) work
#       (dictionary lookup/insertion is O(1) on average, plus one addition).
#       Values 2 through n are each computed once: n - 1 computations.
#       Each computation makes 2 recursive calls, giving 2(n - 1) calls,
#       plus the initial call: 2n - 1.

# Space: O(n): the call stack is at most n frames deep.
#         The dictionary holds n + 1 entries (keys 0 through n, inclusive).
def fib_memo(n):
    if type(n) is not int:
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be a non-negative int")

    memo = {
        0: 0,
        1: 1
    }

    return _fib_memo(n, memo)


def _fib_memo(n, memo):
    global call_count
    call_count += 1

    if n in memo:
        return memo[n]

    memo[n] = _fib_memo(n - 1, memo) + _fib_memo(n - 2, memo)
    return memo[n]
   
   