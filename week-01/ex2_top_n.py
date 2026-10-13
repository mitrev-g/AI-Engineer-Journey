from ex1_word_count import word_count

def top_n_loop(counts, n):
    '''words with the same amount of copies inside the dictionary get inserted based on the order of appearing first in the dictionary keys'''
    if n < 0:
        return []
    remaining = counts.copy()
    res = []
    for _ in range(min(n, len(remaining))):
        largest_key = None
        largest_value = None
        for key, value in remaining.items():
            if largest_value is None or value > largest_value:
                largest_key = key
                largest_value = value
        res.append(largest_key)
        del remaining[largest_key]
    return res

def top_n_sorted(counts, n):
    '''words with the same amount of copies inside the dictionary get inserted based on the order of appearing first in the dictionary keys'''
    if n < 0:
        return []
    result = sorted(counts, key=lambda word: counts[word], reverse=True)
    return result[:n]


counts = word_count("the cat and the dog and the bird")

print(top_n_loop(counts, 2))  # ['the', 'and']
print(top_n_sorted(counts, 2))

for fn in (top_n_loop, top_n_sorted):
    assert fn({"a": 3, "b": 1}, 1) == ["a"]
    assert fn({'b': 2, 'c': 3, "d": 4}, 2) == ['d', 'c']
    assert fn ({"a": 3, "b": 1}, 0) == []
    assert fn({"a": 3, "b": 1}, -2) == []
       # ... ties, n=0, n too big, negative n
    assert fn({"b": 1, "a": 1}, 2) == ["b", "a"]   # ties follow insertion order, as documented
    assert fn({"a": 3, "b": 1}, 10) == ["a", "b"]  # n larger than the number of words