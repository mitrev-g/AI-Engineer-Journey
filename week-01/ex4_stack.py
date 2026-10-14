'''
A Stack class with push, pop, peek and is_empty. 
Use it to write is_balanced("({[]})") → True 
and is_balanced("([)]") → False'''


class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        removed = self.items.pop()
        return removed
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0



def is_balanced(text: str) -> bool:
    s = Stack()
    pairs = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    for ch in text:
        
        if ch in pairs.values():
            s.push(ch)
        elif ch in pairs.keys():
            if pairs[ch] != s.pop():
                return False

    return s.is_empty()


 


if __name__ == "__main__":
  
    assert is_balanced("({[]})") == True
    assert is_balanced("([)]") == False
    assert is_balanced('""') == True
    assert is_balanced("") == True
    assert is_balanced('(", ")') == True
    assert is_balanced("a(b)c") == True
    assert is_balanced("(") == False
    assert is_balanced(")") == False
    assert is_balanced("(]") == False
    assert is_balanced("((") == False

    s = Stack()
    s.push(1); s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1
    assert Stack().pop() is None