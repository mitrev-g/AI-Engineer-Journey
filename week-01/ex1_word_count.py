import string

def word_count(text: str) -> dict[str, int]:
    
    clean_text = "".join(" " if ch in string.punctuation else ch for ch in text)
    words = clean_text.lower().split()
    res = {}
   
    for word in words:
        res[word] = res.get(word, 0) + 1
    return res

if __name__ == "__main__":
    assert word_count("state-of-the-art") == {"state": 1, "of": 1, "the": 1, "art": 1}
    assert word_count("hello, Hello") == {"hello": 2}
    assert word_count("") == {}
    assert word_count("!!!") == {}

