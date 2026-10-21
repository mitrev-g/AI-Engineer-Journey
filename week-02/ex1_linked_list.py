'''
LinkedList, from scratch.
Write a Node class with value and next, 
plus append, prepend, find(value), remove(value), __len__, 
to_list(), and reverse(), which reverses in place with no new list. 
Then compare each operation’s complexity with Python’s list. 
When does a linked list win?


__init__()	Empty list: head, tail and size set to None, None, 0	
append(value)	Add to the end	
prepend(value)	Add to the front	
find(value)	Return True or False for whether the value is in the list	Or return the index? Pick one
remove(value)	Remove the first node with that value	What if it’s not there: do nothing, return False, or raise ValueError?
__len__()	Return size, so len(my_list) works	
to_list()	Return a normal Python list of the values, in order	
reverse()	Reverse the list in place, without building a new list or new nodes	'''

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, data):
        '''
        Creates a new node and adds it after the last one.
        O(1)
        '''
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return
        
        
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        
        

    def prepend(self, data):
        '''
        Creates and adds a new node at the beginning of the linked list.
        O(1)
        '''
        if self.head is None:
            head = Node(data, None)
            self.head = head
            self.tail = head
            self.size += 1
            return
        
        old = self.head
        self.head = Node(data, old)

        self.size += 1
        

    def find(self, value):
        """
        Returns the index of the node with the value.
        Returns -1 if the value is not in the linked list.
        O(n)
        """
        
        idx = 0
        
        itr = self.head
        while itr:
            if itr.data == value:
                return idx
            idx += 1
            itr = itr.next
        
        return -1



        
    def remove(self, value):
        '''
        Searches and removes a node with a given value.
        O(n)
        '''
        if self.head is None:
            return False
        

        if self.head.data == value:
            if self.head.next is None:
                self.size -= 1
                self.head = None
                self.tail = None
                return True
            self.size -= 1
            
            self.head = self.head.next
            return True
            
        
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                self.size -= 1
                if itr.next is self.tail:
                    self.tail = itr
                    itr.next = None
                    
                    return True
                itr.next = itr.next.next
                
                return True
            itr = itr.next

        return False
                

        

        
    def __len__(self):
        # O(1)
        return self.size
    def to_list(self):
        '''
        Converts the linked list to a list
        O(n)
        '''
        res = []
        itr = self.head
        while itr:
            res.append(itr.data)
            itr = itr.next
        return res
    def reverse(self):
        '''
        Reverses the order of the linked list.
        '''
        prev = None # previous on 1st iter is None
        curr = self.head # node 0
        
        head = self.head
        tail = self.tail
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt
        self.tail = head
        self.head = tail
        
        return self


            
        
    


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    assert len(ll1) == 3
    ll1.prepend(0)
    assert len(ll1) == 4
    assert ll1.to_list() == [0, 1, 2, 3]
    empty = LinkedList()
    assert empty.to_list() == []
    assert len(empty) == 0

    ll = LinkedList()
    ll.prepend(5)          # prepend on an empty list
    assert ll.to_list() == [5]
    ll.append(6)           # does tail still work after prepend?
    assert ll.to_list() == [5, 6]
    assert ll1.find(0) == 0     # head
    assert ll1.find(2) == 2     # middle
    assert ll1.find(3) == 3     # tail: the one your old version missed
    assert ll1.find(99) == -1   # missing
    assert empty.find(1) == -1  # empty list
    

    def make(*values):
        ll = LinkedList()
        for v in values:
            ll.append(v)
        return ll
    ll = make(1, 2, 3); assert ll.remove(1) is True;  assert ll.to_list() == [2, 3]   # head
    ll = make(1, 2, 3); assert ll.remove(2) is True;  assert ll.to_list() == [1, 3]   # middle
    ll = make(1, 2, 3); assert ll.remove(3) is True;  assert ll.to_list() == [1, 2]   # tail
    ll.append(4);       assert ll.to_list() == [1, 2, 4]                               # tail updated?
    ll = make(1);       assert ll.remove(1) is True;  assert ll.to_list() == []       # only node
    ll.append(7);       assert ll.to_list() == [7]                                     # head AND tail reset?
    ll = make(1, 2);    assert ll.remove(9) is False; assert len(ll) == 2             # missing
    assert LinkedList().remove(1) is False                                             # empty
    print(ll.reverse())