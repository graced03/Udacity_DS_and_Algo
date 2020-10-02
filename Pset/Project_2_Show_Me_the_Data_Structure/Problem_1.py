from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache= OrderedDict()
        self.max_capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            key_value = self.cache.pop(key)
            self.cache[key] = key_value
            return key_value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.max_capacity == 0:
            print("Cache capacity cannot be 0!")
            return
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.max_capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value

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

print(our_cache.get(9))      
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case 1:
our_cache = LRU_Cache(3)
our_cache.set(1, 10)
our_cache.set(2, 2)
our_cache.set(3, 1)
our_cache.set(2, 3)
print(our_cache.get(1))
# returns 10
print(our_cache.get(2))
# returns 3


# Edge Case 2:
our_cache = LRU_Cache(0)
our_cache.set(10, 10)
# Cache capacity cannot be 0!
print(our_cache.get(10))
# -1