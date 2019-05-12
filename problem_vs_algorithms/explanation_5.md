## Explanation

Basic Trie implementation:
- class TrieNode: Represents a character, has a children dictionary which has the next character mapped to another
TrieNode, and has an `isWordEnd` flag that specifies a word's end.
- class Trie: Uses TrieNode to create a tree structure. Inserts words character by character. Finds words by traversing
the tree.

## Design

Trie class can be used to insert and find words for autocomplete.

## Big O

Word insert => **O(n)**
Find Suffixes => **O(n log(n))**