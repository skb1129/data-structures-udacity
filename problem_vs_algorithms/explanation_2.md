## Explanation

Check the test value with mid item in array. If its not a match, check with left value. If its smaller, move mid to the
right. If its bigger, move mid to the left. If its a match, return left. If mid matches the last mid, return -1.

## Design

Single function that inputs an array and test value to search.

## Big O

**O(log(n))**