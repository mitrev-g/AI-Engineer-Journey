
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



# has_duplicates_brute
# Time Complexity: O(n^2) if there are no duplicates: n(n−1)/2
# Space Complexity: O(1), no additional space needed, we don't store anything
def has_duplicates_brute(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# has_duplicates
# Time Complexity: O(n): O(n) times checks in the set x O(1) work for checking in set
# Space Complexity: O(n): If there are no duplicates, the size of the set will grow to amount of elements in n
def has_duplicates(nums: list[int]) -> bool:
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False



# first_unique_char_brute
# Time: O(n²), n = len(s): for each index, scans the whole string for a twin;
#   worst case (no unique char) n·(n−1) comparisons.
# Space: O(1): only the indices i, j and the flag, a constant amount regardless of n.
def first_unique_char_brute(s: str) -> int:
    for i in range(len(s)):
        duplicate = False

        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                duplicate = True
                break

        if not duplicate:
            return i

    return -1


# first_unique_char
# Time: O(n), n = len(s): one counting pass O(n), one pass over the dict O(k),
#   and s.index runs at most once (it returns), O(n). Total O(n).
#   The dict pass works because dicts keep insertion order (Python 3.7+),
#   so keys come out in order of first appearance.
# Space: O(min(n, k)), k = number of distinct characters possible (the alphabet);
#   O(1) for a fixed alphabet like 26 lowercase letters.
def first_unique_char(s: str) -> int:
    chars: dict[str, int] = {}
    for ch in s:
        chars[ch] = chars.get(ch, 0) + 1 

    for ch in chars:
        if chars[ch] == 1:
            return s.index(ch)
    return -1


# group_anagrams_brute
# Time: O(n² · m log m) worst case, n = number of words, m = max word length:
#   when no words are anagrams, word k compares against k groups → n(n−1)/2
#   comparisons, each re-sorting group[0] at O(m log m).
# Space: O(n · m): the groups store every word (up to m chars each).
def group_anagram_brute(words: list[str]) -> list[list[str]]:
    groups: list[list[str]] = []
    for word in words:
        matching = False
        key = sorted(word)
        for group in groups:
            if sorted(group[0]) == key:
                group.append(word)
                matching = True
                break
        if not matching:
            groups.append([word])
    return groups
        
# group_anagrams
# Time: O(n · m log m), n = number of words, m = max word length:
#   one pass over the words; each key sorts one word's letters, O(m log m),
#   and the dict lookup/insert (hashing an m-char key) is O(m), dominated by the sort.
# Space: O(n · m): the dict's lists hold every word (up to m chars each),
#   plus at most n keys of up to m chars.
def group_anagram(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
