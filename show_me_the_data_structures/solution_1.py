class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

    def get(self, key):
        return self.cache.get(key, -1)

    def set(self, key, value):
        if (key not in self.cache) and (len(self.cache) >= self.capacity):
            deprecated_entry = list(self.cache.keys())[0]
            del self.cache[deprecated_entry]
        self.cache[key] = value


# Test Case: 1
our_cache = LRU_Cache(5)
our_cache.set(7, 7)
our_cache.set(6, 6)
our_cache.set(5, 5)
our_cache.set(4, 4)
our_cache.set(3, 3)
our_cache.set(2, 2)
our_cache.set(1, 1)
print(our_cache.get(7))
print(our_cache.get(2))

# Test Case: 2
our_cache = LRU_Cache(3)
our_cache.set(7, 7)
our_cache.set(6, 6)
our_cache.set(5, 5)
our_cache.set(4, 4)
print(our_cache.get(4))
print(our_cache.get(6))

# Test Case: 3
our_cache = LRU_Cache(1)
our_cache.set(7, 7)
our_cache.set(6, 6)
our_cache.set(5, 5)
our_cache.set(4, 4)
our_cache.set(3, 3)
our_cache.set(2, 2)
our_cache.set(1, 1)
print(our_cache.get(5))
print(our_cache.get(1))