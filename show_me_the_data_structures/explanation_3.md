## Explanation

- Class `Node` is a tree node.
- While encoding, I create an array of nodes from the character frequency dictionary.
- `create_tree` function creates a tree using this nodes array.
- `get_code` function recursively returns a code for each of the character.
- Decoding function traverses the tree using the encoded data and returns the decoded string.

## Big O

**O(n log(n))**