class Queue:
    def __init__(self):
         self.storage = []
    
    def size(self):
         return len(self.storage)
    
    def enqueue(self, item):
         self.storage.append(item)

    def dequeue(self):
         return self.storage.pop(0)


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict()
        self.visit_queue = Queue()
        self.max_capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            self.visit_queue.dequeue()
            self.visit_queue.enqueue(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) == self.max_capacity:
            key_to_remove = self.visit_queue.dequeue()
            del self.cache[key_to_remove]
        self.cache.update({key: value})
        self.visit_queue.enqueue(key)

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

# Testing
# Normal Cases
print(our_cache.get(1))       
# returns 1
print(our_cache.get(2))       
# returns 2

# Edge Cases
print(our_cache.get(9))      
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
