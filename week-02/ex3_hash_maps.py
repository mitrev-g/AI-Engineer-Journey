class HashMap():
    def __init__(self, capacity=8):
        self.buckets = [[] for _ in range(capacity)]   # 8 empty buckets
        self.size = 0
    

    def put(self, key, value):
        index = self._index(key)    # which bucket a key lives in
        bucket = self.buckets[index]
        for idx, el in enumerate(bucket):
            if el[0] == key:
                bucket[idx] = (key, value)
                return
        
        
        bucket.append((key, value))
        self.size += 1
        if self.size / len(self.buckets) > 0.75:
            self._resize()
            


    def get(self, key):
        index = self._index(key)    
        bucket = self.buckets[index]
        
        for el in bucket:
            if el[0] == key:
                return el[1]
        return None

        


    def remove(self, key):
        index = self._index(key)    
        bucket = self.buckets[index]
        for idx, el in enumerate(bucket):
            if el[0] == key:
                bucket.pop(idx)
                self.size -= 1
                return True
        return False
            


    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._index(key)    # which bucket a key lives in
        bucket = self.buckets[index]
        
        for el in bucket:
            if el[0] == key:
                return True
        return False

    def _resize(self):
        old = self.buckets
        self.buckets = [[] for _ in range(2 * len(old))]
        for bucket in old:
            for key, value in bucket:
                index = self._index(key)    # NEW size
                self.buckets[index].append((key, value))

    def _index(self, key):
        return hash(key) % len(self.buckets)










m = HashMap()
m.put([1,2], 3)