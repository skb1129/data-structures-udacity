## Explanation

- The Block has keys `data`, `height`, `hash`, `next`, `time_stamp`.
- `data` and `height` are passed in the block constructor.
- `hash` is calculated using the current time_stamp as a string.
- The BlockChain creates a genesis block in the constructor.
- On creation of each subsequent block, the new block is added to the `next` key of the last block in the chain.

## Big O

**O(n)**