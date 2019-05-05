## Explanation

- I have used python3 dictionaries to store the cache.
- Also, created a separate variable to keep the cache capacity.
- Python dictionaries have many built in components and it has an optimized performance.


## Design

- The `get()` function just returns the value of a specified key.
- The `set()` function first checks if the key is not already present in the dictionary and that the cache capacity is exceeded. Then it removes the oldest key from the cache.

## Big O

**O(1)**